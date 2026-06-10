import json

from services.openai_service import (
    OpenAIService
)


class PlannerAgent:

    def __init__(self):

        self.openai_service = (
            OpenAIService()
        )

    def create_plan(
        self,
        question: str
    ):

        system_prompt = (
            "You are an AI planning agent.\n\n"

            "Available agents:\n"

            "- knowledge\n"
            "- devops\n"
            "- cloudops\n\n"

            "Return ONLY a JSON array.\n\n"

            "Examples:\n"

            "Question: Explain the architecture\n"
            "Response: [\"knowledge\"]\n\n"

            "Question: Show GitHub pull requests\n"
            "Response: [\"devops\"]\n\n"

            "Question: Show Azure cost optimization recommendations\n"
            "Response: [\"cloudops\"]\n\n"

            "Question: Explain architecture and show GitHub information\n"
            "Response: [\"knowledge\", \"devops\"]\n\n"

            "Question: Explain architecture and provide Azure recommendations\n"
            "Response: [\"knowledge\", \"cloudops\"]\n\n"

            "Return only valid JSON."
        )

        try:

            ai_response = (
                self.openai_service
                .generate_response(
                    system_prompt=system_prompt,
                    question=question
                )
            )

            response_text = (
                ai_response["content"]
            )

            plan = json.loads(
                response_text
            )

            valid_agents = {
                "knowledge",
                "devops",
                "cloudops"
            }

            plan = [

                agent

                for agent in plan

                if agent in valid_agents
            ]

            if not plan:

                return [
                    "knowledge"
                ]

            return plan

        except Exception:

            return [
                "knowledge"
            ]
