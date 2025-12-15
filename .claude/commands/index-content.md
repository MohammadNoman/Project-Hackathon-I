---
description: Index content into Qdrant vector database for RAG
---

# Index Content

Index textbook content into Qdrant vector database for RAG-powered chatbot.

## Prerequisites

- Backend running
- Qdrant configured in `.env`
- OpenAI API key configured

## Run Indexing

```bash
cd backend
python -m app.scripts.index_content
```

Or if you have a dedicated script:

```bash
cd backend
python scripts/index_qdrant.py
```

## What Gets Indexed

- Docusaurus markdown files from `frontend/docs/`
- Chapter content
- Section headings
- Code examples (optionally)

## Indexing Process

1. **Load documents** - Read all `.md` files
2. **Chunk content** - Split into manageable pieces (512 tokens)
3. **Generate embeddings** - Using OpenAI `text-embedding-3-small`
4. **Upload to Qdrant** - Store vectors with metadata
5. **Verify** - Test search functionality

## Manual Indexing Code

If script doesn't exist, use this pattern:

```python
# backend/scripts/index_qdrant.py
import os
from pathlib import Path
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# Create collection
qdrant.recreate_collection(
    collection_name="textbook_content",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

# Index documents
docs_path = Path("../frontend/docs")
for md_file in docs_path.rglob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    
    # Generate embedding
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=content[:8000]  # Limit to avoid token limits
    )
    embedding = response.data[0].embedding
    
    # Upload to Qdrant
    qdrant.upsert(
        collection_name="textbook_content",
        points=[
            PointStruct(
                id=hash(str(md_file)),
                vector=embedding,
                payload={
                    "file_path": str(md_file),
                    "content": content[:1000],  # Store preview
                    "title": md_file.stem
                }
            )
        ]
    )
    print(f"Indexed: {md_file}")

print("Indexing complete!")
```

## Verification

Test the indexed content:

```python
# Test search
results = qdrant.search(
    collection_name="textbook_content",
    query_vector=test_embedding,
    limit=5
)

for result in results:
    print(f"Score: {result.score}, File: {result.payload['file_path']}")
```

## Troubleshooting

**No content indexed:** Check docs path is correct
**Embedding errors:** Verify OpenAI API key
**Qdrant connection fails:** Check QDRANT_URL and API key
**Out of tokens:** Reduce chunk size or filter content

## Re-indexing

To re-index (clears old data):

```python
qdrant.recreate_collection(...)  # Clears and recreates
```

To update incrementally:

```python
qdrant.upsert(...)  # Updates existing or adds new
```

## Scheduling

For automatic updates, set up a cron job or GitHub Action:

```yaml
# .github/workflows/index-content.yml
name: Index Content
on:
  push:
    paths:
      - 'frontend/docs/**'
jobs:
  index:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: cd backend && python -m app.scripts.index_content
```
