from pymongo import MongoClient 
from langchain_mongodb import MongoDBAtlasVectorSearch
import os 
from dotenv import load_dotenv,find_dotenv
from embedding_models import embeddings
_=load_dotenv(find_dotenv())
MONGODB_URI=os.environ.get("MONGODB_URI")
DB_NAME="Agro_rag"
COLLECTION_NAME="documents"
INDEX_NAME="vector_index"
client=MongoClient(MONGODB_URI)
db=client[DB_NAME]
collection=db[COLLECTION_NAME]
vector_store=MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name=INDEX_NAME
)
dense=vector_store.as_retriever(search_kwargs={"k":5})

