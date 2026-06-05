from pathlib import Path

from services.ai_search_service import (
    AISearchService
)

service = AISearchService()

documents = [

    {
        "id": "readme",
        "title": "README",
        "content": Path(
            "README.md"
        ).read_text(),
        "source": "README.md"
    },

    {
        "id": "architecture",
        "title": "Architecture",
        "content": Path(
            "docs/architecture.md"
        ).read_text(),
        "source": "docs/architecture.md"
    }
]

result = service.upload_documents(
    documents
)

print(result)
