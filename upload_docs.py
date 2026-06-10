from pathlib import Path

from services.ai_search_service import (
    AISearchService
)

from services.embedding_service import (
    EmbeddingService
)

from services.chunking_service import (
    ChunkingService
)


search_service = AISearchService()

embedding_service = EmbeddingService()

chunking_service = ChunkingService()


documents = []


files = [

    (
        "README",
        "README.md"
    ),

    (
        "Architecture",
        "docs/architecture.md"
    )
]


for title, path in files:

    print(f"Processing {path}")

    content = Path(path).read_text()

    chunks = chunking_service.chunk_text(
        content
    )

    print(
        f"Generated {len(chunks)} chunks"
    )

    for index, chunk in enumerate(chunks):

        print(
            f"Embedding chunk {index + 1}/{len(chunks)}"
        )

        embedding = (
            embedding_service
            .generate_embedding(chunk)
        )

        documents.append(

            {
                "id": (
                    f"{title.lower()}-{index}"
                ),

                "title": title,

                "content": chunk,

                "source": path,

                "contentVector": embedding
            }
        )


print(
    f"\nUploading {len(documents)} chunks..."
)

result = search_service.upload_documents(
    documents
)

print(
    f"Successfully uploaded {len(documents)} chunks"
)

print(result)
