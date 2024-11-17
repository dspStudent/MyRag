from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from qdrant_client.http.models import Distance, VectorParams
import os
import constants as const
import Embeddings.huggingface_embeddings as he

qdrant_client=QdrantClient(
    url="https://dd22169f-0c45-4259-8909-8dcf31aead3e.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="SY1sJVZJ0ABQX0fh1W5JHDLkY1fSV4187D1-eaEqolASRORXw6O6nA"
)

vector_store = QdrantVectorStore(
    client=qdrant_client,
    collection_name="my_rag_col",
    embedding=he.embeddings
)

vector_store_user_train = QdrantVectorStore(
    client=qdrant_client,
    collection_name="my_rag_user_train",
    embedding=he.embeddings
)

def add_content(content):
    vector_store.add_documents(content)

def add_content_user(content):
    vector_store_user_train.add_documents(content)

def retrieve_content(content, k):
    return vector_store.similarity_search(content, k=k)


def retrieve_content_user(content, k):
    return vector_store_user_train.similarity_search(content, k=k)