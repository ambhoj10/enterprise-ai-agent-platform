import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    # --------------------------------------------------
    # Azure OpenAI
    # --------------------------------------------------

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    AZURE_OPENAI_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    )

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    )

    # --------------------------------------------------
    # Azure AI Search
    # --------------------------------------------------

    AZURE_SEARCH_ENDPOINT = os.getenv(
        "AZURE_SEARCH_ENDPOINT"
    )

    AZURE_SEARCH_API_KEY = os.getenv(
        "AZURE_SEARCH_API_KEY"
    )

    AZURE_SEARCH_INDEX = os.getenv(
        "AZURE_SEARCH_INDEX"
    )

    # --------------------------------------------------
    # GitHub Integration
    # --------------------------------------------------

    GITHUB_TOKEN = os.getenv(
        "GITHUB_TOKEN"
    )

    GITHUB_OWNER = os.getenv(
        "GITHUB_OWNER"
    )

    # --------------------------------------------------
    # Azure DevOps Integration
    # --------------------------------------------------

    AZURE_DEVOPS_ORG = os.getenv(
        "AZURE_DEVOPS_ORG"
    )

    AZURE_DEVOPS_PROJECT = os.getenv(
        "AZURE_DEVOPS_PROJECT"
    )

    AZURE_DEVOPS_PAT = os.getenv(
        "AZURE_DEVOPS_PAT"
    )

    # --------------------------------------------------
    # JWT Authentication
    # --------------------------------------------------

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY"
    )

    JWT_ALGORITHM = os.getenv(
        "JWT_ALGORITHM",
        "HS256"
    )

    JWT_EXPIRATION_MINUTES = int(
        os.getenv(
            "JWT_EXPIRATION_MINUTES",
            "60"
        )
    )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self):

        required_settings = {

            "AZURE_OPENAI_ENDPOINT":
                self.AZURE_OPENAI_ENDPOINT,

            "AZURE_OPENAI_API_KEY":
                self.AZURE_OPENAI_API_KEY,

            "AZURE_OPENAI_DEPLOYMENT":
                self.AZURE_OPENAI_DEPLOYMENT,

            "JWT_SECRET_KEY":
                self.JWT_SECRET_KEY
        }

        missing = [

            key

            for key, value
            in required_settings.items()

            if not value
        ]

        if missing:

            raise ValueError(

                "Missing required configuration: "

                + ", ".join(
                    missing
                )
            )


settings = Settings()

settings.validate()
