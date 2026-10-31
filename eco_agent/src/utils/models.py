from langchain_groq import ChatGroq 
from dotenv import load_dotenv,find_dotenv
import os 
_=load_dotenv(find_dotenv())
key=os.environ.get("GROQ_API_KEY")
llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0,api_key=key)
