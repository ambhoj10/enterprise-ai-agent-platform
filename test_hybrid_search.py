from services.ai_search_service import (
    AISearchService
)

service = AISearchService()

results = service.search_client.search(
    search_text="architecture",
    top=5
)

for doc in results:

    print(doc["source"])
