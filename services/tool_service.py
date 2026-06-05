from services.tools.github_tool import GitHubTool
from services.tools.azure_devops_tool import AzureDevOpsTool
from services.tools.search_tool import SearchTool


class ToolService:

    def __init__(self):

        self.github_tool = GitHubTool()
        self.azure_devops_tool = AzureDevOpsTool()
        self.search_tool = SearchTool()

    # GitHub

    def get_github_context(self):

        return "\n".join(
            self.github_tool.get_best_practices()
        )

    def get_repository_summary(
        self,
        repository_name
    ):

        return self.github_tool.get_repository_summary(
            repository_name
        )

    def get_open_issues(
        self,
        repository_name
    ):

        return self.github_tool.get_open_issues(
            repository_name
        )

    def get_pull_requests(
        self,
        repository_name
    ):

        return self.github_tool.get_pull_requests(
            repository_name
        )

    def get_workflow_runs(
        self,
        repository_name
    ):

        return self.github_tool.get_workflow_runs(
            repository_name
        )

    # Azure DevOps

    def get_azure_devops_context(self):

        return "\n".join(
            self.azure_devops_tool.get_best_practices()
        )

    def get_pipeline_summary(self):

        return (
            self.azure_devops_tool.get_pipeline_summary()
        )

    def get_build_summary(self):

        return (
            self.azure_devops_tool.get_build_summary()
        )

    # Search / Retrieval

    def search_knowledge(
        self,
        query
    ):

        return self.search_tool.search_knowledge_base(
            query
        )
