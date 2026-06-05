from services.ai_search_service import (
    AISearchService
)


class SearchTool:

    def __init__(self):

        self.ai_search_service = (
            AISearchService()
        )

    def search_knowledge_base(
        self,
        query
    ):

        results = (
            self.ai_search_service
            .search_documents(query)
        )

        if not results:

            return "No knowledge found."

        return "\n\n".join(
            (
                f"Title: {result['title']}\n"
                f"Source: {result['source']}\n"
                f"Content:\n{result['content']}"
            )
            for result in results[:3]
        )
