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

    # GitHub Integration

    GITHUB_TOKEN = os.getenv(
        "GITHUB_TOKEN"
    )

    GITHUB_OWNER = os.getenv(
        "GITHUB_OWNER"
    )


settings = Settings()
