import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    # Azure OpenAI

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    AZURE_OPENAI_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    )

    # Azure AI Search

    AZURE_SEARCH_ENDPOINT = os.getenv(
        "AZURE_SEARCH_ENDPOINT"
    )

    AZURE_SEARCH_API_KEY = os.getenv(
        "AZURE_SEARCH_API_KEY"
    )

    AZURE_SEARCH_INDEX = os.getenv(
        "AZURE_SEARCH_INDEX"
    )

    # GitHub Integration

    GITHUB_TOKEN = os.getenv(
        "GITHUB_TOKEN"
    )

    GITHUB_OWNER = os.getenv(
        "GITHUB_OWNER"
    )

    # Azure DevOps Integration

    AZURE_DEVOPS_ORG = os.getenv(
        "AZURE_DEVOPS_ORG"
    )

    AZURE_DEVOPS_PROJECT = os.getenv(
        "AZURE_DEVOPS_PROJECT"
    )

    AZURE_DEVOPS_PAT = os.getenv(
        "AZURE_DEVOPS_PAT"
    )


settings = Settings()
