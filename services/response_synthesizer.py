from services.openai_service import (
    OpenAIService
)


class ResponseSynthesizer:

    def __init__(self):

        self.openai_service = (
            OpenAIService()
        )

    def synthesize(
        self,
        question,
        agent_results
    ):

        context = "\n\n".join(

            (
                f"Agent: {result['agent']}\n"
                f"Response:\n{result['response']}"
            )

            for result in agent_results
        )

        system_prompt = (
            "You are an Enterprise AI Orchestrator.\n\n"

            "Your responsibility is to synthesize "
            "responses from multiple agents into a "
            "single business response.\n\n"

            "STRICT RULES:\n"

            "- Use ONLY information provided in the "
            "agent responses.\n"

            "- Do NOT invent facts.\n"

            "- Do NOT invent capabilities.\n"

            "- Do NOT add information that is not "
            "present in the agent responses.\n"

            "- If information is missing, explicitly "
            "state that it was not provided.\n"

            "- Clearly indicate which findings came "
            "from which agent.\n\n"

            "Agent Responses:\n\n"
            f"{context}\n\n"

            "Generate a response using:\n"
            "1. Executive Summary\n"
            "2. Key Findings\n"
            "3. Agent Contributions\n"
            "4. Recommended Actions\n"
            "5. Information Gaps (if any)\n"
        )

        ai_response = (
            self.openai_service
            .generate_response(
                system_prompt=system_prompt,
                question=question
            )
        )

        return {

            "response":
                ai_response["content"],

            "prompt_tokens":
                ai_response["prompt_tokens"],

            "completion_tokens":
                ai_response["completion_tokens"],

            "total_tokens":
                ai_response["total_tokens"]
        }
