from services.ai_search_service import (
    AISearchService
)

service = AISearchService()

results = service.search_hybrid_documents(
    "How does the multi-agent architecture work?"
)

print(f"Found {len(results)} results\n")

for result in results:

    print("=" * 60)
    print(f"Source: {result['source']}")
    print(result["content"][:300])
    print()
