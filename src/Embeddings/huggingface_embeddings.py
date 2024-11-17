from langchain_huggingface import HuggingFaceEmbeddings

embeddings1=HuggingFaceEmbeddings(
    model_name="jinaai/jina-embeddings-v2-base-en"
)
embeddings=HuggingFaceEmbeddings(
    model_name="AnnaWegmann/Style-Embedding"
)