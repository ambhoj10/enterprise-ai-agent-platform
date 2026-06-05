from azure.core.credentials import (
    AzureKeyCredential
)

from azure.search.documents import (
    SearchClient
)

from azure.search.documents.indexes import (
    SearchIndexClient
)

from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchFieldDataType
)

from app.config import settings


class AISearchService:

    def __init__(self):

        credential = AzureKeyCredential(
            settings.AZURE_SEARCH_API_KEY
        )

        self.index_client = (
            SearchIndexClient(
                endpoint=settings.AZURE_SEARCH_ENDPOINT,
                credential=credential
            )
        )

        self.search_client = (
            SearchClient(
                endpoint=settings.AZURE_SEARCH_ENDPOINT,
                index_name=settings.AZURE_SEARCH_INDEX,
                credential=credential
            )
        )

    def create_index(self):

        fields = [

            SimpleField(
                name="id",
                type=SearchFieldDataType.String,
                key=True
            ),

            SearchableField(
                name="title",
                type=SearchFieldDataType.String
            ),

            SearchableField(
                name="content",
                type=SearchFieldDataType.String
            ),

            SimpleField(
                name="source",
                type=SearchFieldDataType.String
            )
        ]

        index = SearchIndex(
            name=settings.AZURE_SEARCH_INDEX,
            fields=fields
        )

        return self.index_client.create_or_update_index(
            index
        )

    def upload_documents(
        self,
        documents
    ):

        return self.search_client.upload_documents(
            documents
        )

    def search_documents(
        self,
        query
    ):

        results = self.search_client.search(
            search_text=query
        )

        return [
            {
                "title": doc["title"],
                "source": doc["source"]
            }
            for doc in results
        ]
