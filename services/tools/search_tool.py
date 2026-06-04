class SearchTool:

    def search_knowledge_base(
        self,
        query
    ):

        knowledge = {
            "rag": (
                "Retrieval Augmented Generation combines "
                "retrieval systems with LLMs to provide "
                "grounded responses."
            ),
            "azure ai search": (
                "Azure AI Search is Microsoft's enterprise "
                "search and retrieval platform."
            ),
            "agent": (
                "An AI agent is a system that can reason, "
                "use tools, and perform tasks."
            )
        }

        query = query.lower()

        for key, value in knowledge.items():

            if key in query:

                return value

        return "No knowledge found."
