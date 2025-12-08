"""Setup Qdrant collection for Physical AI Textbook RAG system.

Usage:
    python -m scripts.setup_qdrant [--recreate] [--verify]
"""

import sys
import os
import argparse

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PayloadSchemaType
from app.core.config import settings

COLLECTION_NAME = "physical_ai_textbook"
EMBEDDING_DIMENSION = 1536  # text-embedding-3-small


def get_client() -> QdrantClient:
    """Get Qdrant client based on settings."""
    if settings.qdrant_api_key:
        return QdrantClient(
            url=settings.qdrant_host,
            api_key=settings.qdrant_api_key,
            timeout=30.0
        )
    return QdrantClient(host=settings.qdrant_host, port=6333, timeout=30.0)


def create_collection(client: QdrantClient, recreate: bool = False) -> None:
    """Create Qdrant collection with proper configuration."""
    collections = client.get_collections().collections
    exists = any(c.name == COLLECTION_NAME for c in collections)

    if exists:
        if recreate:
            print(f"Deleting existing collection: {COLLECTION_NAME}")
            client.delete_collection(collection_name=COLLECTION_NAME)
        else:
            print(f"Collection '{COLLECTION_NAME}' already exists. Use --recreate to overwrite.")
            return

    print(f"Creating collection: {COLLECTION_NAME}")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=EMBEDDING_DIMENSION,
            distance=Distance.COSINE
        )
    )

    # Create payload indexes
    print("Creating payload indexes...")
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="file",
        field_schema=PayloadSchemaType.KEYWORD
    )
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="section",
        field_schema=PayloadSchemaType.TEXT
    )
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="chunk_index",
        field_schema=PayloadSchemaType.INTEGER
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully!")


def verify_collection(client: QdrantClient) -> None:
    """Verify collection configuration."""
    info = client.get_collection(collection_name=COLLECTION_NAME)
    print(f"\nCollection Info:")
    print(f"  Vector size: {info.config.params.vectors.size}")
    print(f"  Distance: {info.config.params.vectors.distance}")
    print(f"  Points count: {info.points_count}")


def main():
    parser = argparse.ArgumentParser(description="Setup Qdrant collection")
    parser.add_argument("--recreate", action="store_true", help="Recreate collection if exists")
    parser.add_argument("--verify", action="store_true", help="Verify collection after creation")
    args = parser.parse_args()

    print(f"Connecting to Qdrant at {settings.qdrant_host}...")

    try:
        client = get_client()
        collections = client.get_collections()
        print(f"Connected! Found {len(collections.collections)} collections.")

        create_collection(client, recreate=args.recreate)

        if args.verify:
            verify_collection(client)

        print("\nSetup complete!")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
