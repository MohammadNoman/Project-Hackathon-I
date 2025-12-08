"""Index Physical AI Textbook content into Qdrant for RAG.

Usage:
    python -m scripts.index_content [--force] [--batch-size 50]
"""

import sys
import os
import re
import hashlib
import argparse
import time
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from openai import OpenAI
from app.core.config import settings

COLLECTION_NAME = "physical_ai_textbook"
EMBEDDING_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
BATCH_SIZE = 50


@dataclass
class ContentChunk:
    """A chunk of textbook content."""
    text: str
    file: str
    section: str
    chunk_index: int
    doc_id: str


class ContentIndexer:
    """Handles content indexing operations."""

    def __init__(self, docs_dir: Path):
        self.docs_dir = docs_dir
        self.openai_client = OpenAI(api_key=settings.openai_api_key)

        if settings.qdrant_api_key:
            self.qdrant_client = QdrantClient(
                url=settings.qdrant_host,
                api_key=settings.qdrant_api_key,
                timeout=60.0
            )
        else:
            self.qdrant_client = QdrantClient(
                host=settings.qdrant_host,
                port=6333,
                timeout=60.0
            )

    def extract_sections(self, content: str) -> List[Tuple[str, str]]:
        """Extract sections from MDX content based on headers."""
        # Remove frontmatter
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

        sections = []
        lines = content.split('\n')
        current_title = "Introduction"
        current_content = []

        for line in lines:
            header_match = re.match(r'^#{2,3}\s+(.+)$', line)
            if header_match:
                if current_content:
                    sections.append((current_title, '\n'.join(current_content).strip()))
                current_title = header_match.group(1).strip()
                current_content = []
            else:
                current_content.append(line)

        if current_content:
            sections.append((current_title, '\n'.join(current_content).strip()))

        return sections

    def chunk_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks."""
        text = re.sub(r'\s+', ' ', text).strip()

        if len(text) <= CHUNK_SIZE:
            return [text] if text else []

        chunks = []
        start = 0

        while start < len(text):
            end = start + CHUNK_SIZE

            if end < len(text):
                # Try to break at sentence boundary
                sentence_end = text.rfind('. ', end - 100, end + 100)
                if sentence_end != -1:
                    end = sentence_end + 1

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            start = end - CHUNK_OVERLAP

        return chunks

    def process_file(self, file_path: Path) -> List[ContentChunk]:
        """Process a single MDX file into content chunks."""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  Error reading {file_path}: {e}")
            return []

        rel_path = str(file_path.relative_to(self.docs_dir))
        doc_id = hashlib.md5(rel_path.encode()).hexdigest()[:16]

        sections = self.extract_sections(content)
        chunks = []

        for section_title, section_content in sections:
            if not section_content.strip() or len(section_content.strip()) < 50:
                continue

            text_chunks = self.chunk_text(section_content)

            for idx, chunk_text in enumerate(text_chunks):
                chunks.append(ContentChunk(
                    text=chunk_text,
                    file=rel_path,
                    section=section_title,
                    chunk_index=idx,
                    doc_id=doc_id
                ))

        return chunks

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        response = self.openai_client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=texts
        )
        return [item.embedding for item in response.data]

    def index_chunks(self, chunks: List[ContentChunk], batch_size: int = BATCH_SIZE) -> int:
        """Index content chunks into Qdrant."""
        if not chunks:
            print("No chunks to index")
            return 0

        print(f"\nIndexing {len(chunks)} chunks...")
        indexed = 0

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]

            try:
                embeddings = self.generate_embeddings([c.text for c in batch])

                points = [
                    PointStruct(
                        id=f"{chunk.doc_id}_{chunk.chunk_index}_{idx}",
                        vector=embedding,
                        payload={
                            "text": chunk.text,
                            "file": chunk.file,
                            "section": chunk.section,
                            "chunk_index": chunk.chunk_index,
                        }
                    )
                    for idx, (chunk, embedding) in enumerate(zip(batch, embeddings))
                ]

                self.qdrant_client.upsert(
                    collection_name=COLLECTION_NAME,
                    points=points
                )

                indexed += len(points)
                print(f"  Batch {i // batch_size + 1}: {len(points)} chunks indexed")
                time.sleep(0.5)  # Rate limiting

            except Exception as e:
                print(f"  Error in batch {i // batch_size + 1}: {e}")

        return indexed

    def index_all(self, batch_size: int = BATCH_SIZE) -> Dict[str, int]:
        """Index all MDX files from docs directory."""
        mdx_files = list(self.docs_dir.rglob("*.md")) + list(self.docs_dir.rglob("*.mdx"))

        if not mdx_files:
            print(f"No MDX files found in {self.docs_dir}")
            return {"files": 0, "chunks": 0, "indexed": 0}

        print(f"Found {len(mdx_files)} MDX files")

        all_chunks = []
        for file_path in mdx_files:
            print(f"Processing: {file_path.relative_to(self.docs_dir)}")
            chunks = self.process_file(file_path)
            all_chunks.extend(chunks)
            print(f"  -> {len(chunks)} chunks")

        print(f"\nTotal chunks: {len(all_chunks)}")

        indexed = self.index_chunks(all_chunks, batch_size)

        return {
            "files": len(mdx_files),
            "chunks": len(all_chunks),
            "indexed": indexed
        }


def main():
    parser = argparse.ArgumentParser(description="Index textbook content into Qdrant")
    parser.add_argument("--force", action="store_true", help="Force re-indexing")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="Batch size")
    args = parser.parse_args()

    # Find docs directory
    backend_dir = Path(__file__).parent.parent
    docs_dir = backend_dir.parent / "frontend" / "docs"

    if not docs_dir.exists():
        print(f"Docs directory not found: {docs_dir}")
        sys.exit(1)

    print(f"Docs directory: {docs_dir}")
    print(f"Qdrant host: {settings.qdrant_host}")
    print(f"Embedding model: {EMBEDDING_MODEL}")

    try:
        indexer = ContentIndexer(docs_dir)

        # Verify collection exists
        collections = indexer.qdrant_client.get_collections()
        if not any(c.name == COLLECTION_NAME for c in collections.collections):
            print(f"Collection '{COLLECTION_NAME}' not found!")
            print("Run: python -m scripts.setup_qdrant")
            sys.exit(1)

        stats = indexer.index_all(batch_size=args.batch_size)

        print(f"\nIndexing complete!")
        print(f"  Files: {stats['files']}")
        print(f"  Chunks: {stats['chunks']}")
        print(f"  Indexed: {stats['indexed']}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
