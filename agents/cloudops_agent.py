from services.openai_service import OpenAIService


class CloudOpsAgent:

    def __init__(self):

        self.openai_service = OpenAIService()

    def execute(
        self,
        question
    ):

        return {
            "agent": "CloudOps Agent",
            "response": self.openai_service.generate_response(
                system_prompt=(
                    "You are a senior Azure Cloud Architect. "
                    "Provide expert guidance on Azure "
                    "architecture, cost optimization, "
                    "monitoring, reliability, and operations."
                ),
                question=question
            )
        }
