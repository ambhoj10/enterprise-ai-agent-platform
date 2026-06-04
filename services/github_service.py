import requests

from app.config import settings


class GitHubService:

    BASE_URL = "https://api.github.com"

    def _headers(self):

        return {
            "Authorization": (
                f"Bearer {settings.GITHUB_TOKEN}"
            ),
            "Accept": (
                "application/vnd.github+json"
            )
        }

    def get_repository(
        self,
        repository_name
    ):

        response = requests.get(
            f"{self.BASE_URL}/repos/"
            f"{settings.GITHUB_OWNER}/"
            f"{repository_name}",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()

    def get_open_issues(
        self,
        repository_name
    ):

        response = requests.get(
            f"{self.BASE_URL}/repos/"
            f"{settings.GITHUB_OWNER}/"
            f"{repository_name}/issues",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()

    def get_pull_requests(
        self,
        repository_name
    ):

        response = requests.get(
            f"{self.BASE_URL}/repos/"
            f"{settings.GITHUB_OWNER}/"
            f"{repository_name}/pulls",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()

    def get_workflow_runs(
        self,
        repository_name
    ):

        response = requests.get(
            f"{self.BASE_URL}/repos/"
            f"{settings.GITHUB_OWNER}/"
            f"{repository_name}/actions/runs",
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()
