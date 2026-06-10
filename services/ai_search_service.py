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
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration
)

from azure.search.documents.models import (
    VectorizedQuery
)

from app.config import settings

from services.embedding_service import (
    EmbeddingService
)


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

        self.embedding_service = (
            EmbeddingService()
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
            ),

            SearchField(
                name="contentVector",
                type=SearchFieldDataType.Collection(
                    SearchFieldDataType.Single
                ),
                searchable=True,
                vector_search_dimensions=1536,
                vector_search_profile_name="default"
            )
        ]

        vector_search = VectorSearch(
            algorithms=[
                HnswAlgorithmConfiguration(
                    name="hnsw"
                )
            ],
            profiles=[
                VectorSearchProfile(
                    name="default",
                    algorithm_configuration_name="hnsw"
                )
            ]
        )

        index = SearchIndex(
            name=settings.AZURE_SEARCH_INDEX,
            fields=fields,
            vector_search=vector_search
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

    # Keyword Search

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
                "content": doc["content"],
                "source": doc["source"]
            }
            for doc in results
        ]

    # Vector Search

    def search_vector_documents(
        self,
        query,
        top_k=5
    ):

        embedding = (
            self.embedding_service
            .generate_embedding(query)
        )

        vector_query = VectorizedQuery(
            vector=embedding,
            k_nearest_neighbors=top_k,
            fields="contentVector"
        )

        results = self.search_client.search(
            search_text=None,
            vector_queries=[vector_query]
        )

        return [
            {
                "title": doc["title"],
                "content": doc["content"],
                "source": doc["source"]
            }
            for doc in results
        ]

    # Hybrid Search

    def search_hybrid_documents(
        self,
        query,
        top_k=5
    ):

        embedding = (
            self.embedding_service
            .generate_embedding(query)
        )

        vector_query = VectorizedQuery(
            vector=embedding,
            k_nearest_neighbors=top_k,
            fields="contentVector"
        )

        results = self.search_client.search(
            search_text=query,
            vector_queries=[vector_query],
            top=top_k
        )

        return [
            {
                "title": doc["title"],
                "content": doc["content"],
                "source": doc["source"]
            }
            for doc in results
        ]
