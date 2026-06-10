from agents.knowledge_agent import (
    KnowledgeAgent
)

from agents.devops_agent import (
    DevOpsAgent
)

from agents.cloudops_agent import (
    CloudOpsAgent
)


class MultiAgentExecutor:

    def __init__(self):

        self.knowledge_agent = (
            KnowledgeAgent()
        )

        self.devops_agent = (
            DevOpsAgent()
        )

        self.cloudops_agent = (
            CloudOpsAgent()
        )

    def execute(
        self,
        question,
        plan,
        conversation_context=None
    ):

        results = []

        enriched_question = question

        if conversation_context:

            enriched_question = (
                f"Conversation History:\n"
                f"{conversation_context}\n\n"
                f"Current Question:\n"
                f"{question}"
            )

        for agent_name in plan:

            if agent_name == "knowledge":

                results.append(
                    self.knowledge_agent.execute(
                        enriched_question
                    )
                )

            elif agent_name == "devops":

                results.append(
                    self.devops_agent.execute(
                        enriched_question
                    )
                )

            elif agent_name == "cloudops":

                results.append(
                    self.cloudops_agent.execute(
                        enriched_question
                    )
                )

        return results
