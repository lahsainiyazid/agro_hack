from langchain_groq import ChatGroq 
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())
with open("./expansion_model.md","r",encoding="utf-8") as f:
    expansion=f.read()
with open("./answer_model.md","r",encoding="utf-8") as f:
    answer=f.read()
expansion_model=ChatGroq(model=expansion.strip(),temperature=0)
answer_model=ChatGroq(model=answer.strip(),temperature=0)
