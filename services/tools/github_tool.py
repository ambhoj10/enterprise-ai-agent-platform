from services.github_service import GitHubService


class GitHubTool:

    def __init__(self):

        self.github_service = GitHubService()

    def get_best_practices(self):

        return [
            "Use branch protection rules",
            "Enable pull request reviews",
            "Implement GitHub Actions CI/CD",
            "Use Dependabot for dependency updates",
            "Store secrets in GitHub Secrets",
            "Use reusable workflows",
            "Monitor workflow failures"
        ]

    def get_repository_summary(
        self,
        repository_name
    ):

        repo = self.github_service.get_repository(
            repository_name
        )

        return (
            f"Repository: {repo['name']}\n"
            f"Description: {repo.get('description', 'N/A')}\n"
            f"Stars: {repo['stargazers_count']}\n"
            f"Forks: {repo['forks_count']}\n"
            f"Open Issues: {repo['open_issues_count']}"
        )

    def get_open_issues(
        self,
        repository_name
    ):

        issues = self.github_service.get_open_issues(
            repository_name
        )

        if not issues:
            return "No open issues found."

        return "\n".join(
            issue["title"]
            for issue in issues[:5]
        )

    def get_pull_requests(
        self,
        repository_name
    ):

        pull_requests = (
            self.github_service.get_pull_requests(
                repository_name
            )
        )

        if not pull_requests:
            return "No open pull requests found."

        return "\n".join(
            pr["title"]
            for pr in pull_requests[:5]
        )

    def get_workflow_runs(
        self,
        repository_name
    ):

        workflows = (
            self.github_service.get_workflow_runs(
                repository_name
            )
        )

        runs = workflows.get(
            "workflow_runs",
            []
        )

        if not runs:
            return "No workflow runs found."

        return "\n".join(
            (
                f"{run['name']} - "
                f"{run['status']} - "
                f"{run['conclusion']}"
            )
            for run in runs[:5]
        )
