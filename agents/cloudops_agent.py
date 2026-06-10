from services.openai_service import OpenAIService


class CloudOpsAgent:

    def __init__(self):

        self.openai_service = OpenAIService()

    def execute(
        self,
        question
    ):

        ai_response = (
            self.openai_service.generate_response(
                system_prompt=(
                    "You are a senior Azure Cloud Architect. "
                    "Provide expert guidance on Azure "
                    "architecture, cost optimization, "
                    "monitoring, reliability, and operations."
                ),
                question=question
            )
        )

        return {

            "agent":
                "CloudOps Agent",

            "response":
                ai_response["content"],

            "prompt_tokens":
                ai_response["prompt_tokens"],

            "completion_tokens":
                ai_response["completion_tokens"],

            "total_tokens":
                ai_response["total_tokens"]
        }
