from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(
    model_name="jinaai/jina-embeddings-v2-base-en"
)