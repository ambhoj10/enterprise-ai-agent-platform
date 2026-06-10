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

        ai_response = (
            self.openai_service.generate_response(
                system_prompt=(
                    "You are an enterprise knowledge assistant.\n\n"
                    "Knowledge Context:\n"
                    f"{knowledge_context}"
                ),
                question=question
            )
        )

        return {

            "agent":
                "Knowledge Agent",

            "response":
                ai_response["content"],

            "prompt_tokens":
                ai_response["prompt_tokens"],

            "completion_tokens":
                ai_response["completion_tokens"],

            "total_tokens":
                ai_response["total_tokens"]
        }
