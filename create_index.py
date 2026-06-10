from services.ai_search_service import (
    AISearchService
)

service = AISearchService()

service.create_index()

print("Vector index created successfully")
