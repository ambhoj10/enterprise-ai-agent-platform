from services.tools.github_tool import GitHubTool
from services.tools.azure_devops_tool import AzureDevOpsTool
from services.tools.search_tool import SearchTool


class ToolService:

    def __init__(self):

        self.github_tool = GitHubTool()
        self.azure_devops_tool = AzureDevOpsTool()
        self.search_tool = SearchTool()

    def get_github_context(self):

        return "\n".join(
            self.github_tool.get_best_practices()
        )

    def get_azure_devops_context(self):

        return "\n".join(
            self.azure_devops_tool.get_best_practices()
        )

    def search_knowledge(
        self,
        query
    ):

        return self.search_tool.search_knowledge_base(
            query
        )
