from services.openai_service import OpenAIService


class DocumentationAgent:

    def __init__(self):

        self.openai_service = OpenAIService()

    def execute(
        self,
        question
    ):

        return {
            "agent": "Documentation Agent",
            "response": self.openai_service.generate_response(
                system_prompt=(
                    "You are an expert technical writer. "
                    "Create professional enterprise documentation, "
                    "runbooks, SOPs, architecture documents, "
                    "deployment procedures, and operational guides. "
                    "Use clear headings, numbered steps, and "
                    "professional formatting."
                ),
                question=question
            )
        }
