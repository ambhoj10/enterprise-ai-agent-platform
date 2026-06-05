import base64
import requests

from app.config import settings


class AzureDevOpsService:

    BASE_URL = (
        "https://dev.azure.com"
    )

    def _headers(self):

        token = base64.b64encode(
            f":{settings.AZURE_DEVOPS_PAT}".encode()
        ).decode()

        return {
            "Authorization": (
                f"Basic {token}"
            )
        }

    def get_projects(self):

        response = requests.get(
            (
                f"{self.BASE_URL}/"
                f"{settings.AZURE_DEVOPS_ORG}"
                "/_apis/projects"
                "?api-version=7.1-preview.4"
            ),
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()

    def get_pipelines(self):

        response = requests.get(
            (
                f"{self.BASE_URL}/"
                f"{settings.AZURE_DEVOPS_ORG}/"
                f"{settings.AZURE_DEVOPS_PROJECT}"
                "/_apis/pipelines"
                "?api-version=7.1-preview.1"
            ),
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()

    def get_builds(self):

        response = requests.get(
            (
                f"{self.BASE_URL}/"
                f"{settings.AZURE_DEVOPS_ORG}/"
                f"{settings.AZURE_DEVOPS_PROJECT}"
                "/_apis/build/builds"
                "?api-version=7.1-preview.7"
            ),
            headers=self._headers()
        )

        response.raise_for_status()

        return response.json()
