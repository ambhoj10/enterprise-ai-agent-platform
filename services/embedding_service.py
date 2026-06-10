from openai import AzureOpenAI

from app.config import settings


class EmbeddingService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version="2024-02-15-preview",
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
        )

    def generate_embedding(
        self,
        text
    ):

        response = (
            self.client.embeddings.create(
                model=(
                    settings
                    .AZURE_OPENAI_EMBEDDING_DEPLOYMENT
                ),
                input=text
            )
        )

        return response.data[0].embedding
