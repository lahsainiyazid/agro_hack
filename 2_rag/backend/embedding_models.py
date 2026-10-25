from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder

embeddings= HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-large",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

reranker = CrossEncoder("BAAI/bge-reranker-base")
