from services.openai_service import OpenAIService
from services.tool_service import ToolService


class DevOpsAgent:

    def __init__(self):

        self.openai_service = OpenAIService()
        self.tool_service = ToolService()

    def execute(
        self,
        question
    ):

        github_context = (
            self.tool_service.get_github_context()
        )

        azure_devops_context = (
            self.tool_service.get_azure_devops_context()
        )

        repository_context = (
            self.tool_service.get_repository_summary(
                "enterprise-ai-agent-platform"
            )
        )

        issues_context = (
            self.tool_service.get_open_issues(
                "enterprise-ai-agent-platform"
            )
        )

        pull_request_context = (
            self.tool_service.get_pull_requests(
                "enterprise-ai-agent-platform"
            )
        )

        return {
            "agent": "DevOps Agent",
            "response": self.openai_service.generate_response(
                system_prompt=(
                    "You are a senior DevOps engineer.\n\n"

                    "Repository Information:\n"
                    f"{repository_context}\n\n"

                    "Open Issues:\n"
                    f"{issues_context}\n\n"

                    "Open Pull Requests:\n"
                    f"{pull_request_context}\n\n"

                    "GitHub Best Practices:\n"
                    f"{github_context}\n\n"

                    "Azure DevOps Best Practices:\n"
                    f"{azure_devops_context}"
                ),
                question=question
            )
        }
