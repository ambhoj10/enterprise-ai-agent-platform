from services.openai_service import OpenAIService
from services.tool_service import ToolService


class KnowledgeAgent:

    def __init__(self):

        self.openai_service = OpenAIService()
        self.tool_service = ToolService()

    def execute(
        self,
        question
    ):

        knowledge_context = (
            self.tool_service.search_knowledge(
                question
            )
        )

        return {
            "agent": "Knowledge Agent",
            "response": self.openai_service.generate_response(
                system_prompt=(
                    "You are an enterprise knowledge assistant.\n\n"
                    "Knowledge Context:\n"
                    f"{knowledge_context}"
                ),
                question=question
            )
        }
