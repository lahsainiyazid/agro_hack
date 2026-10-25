from langchain_groq import ChatGroq 
from dotenv import load_dotenv,find_dotenv
from pathlib import Path 
PARENT_DIR=Path(__file__).resolve().parent 
_=load_dotenv(find_dotenv())
with open(PARENT_DIR/"expansion_model.md","r",encoding="utf-8") as f:
    expansion=f.read()
with open(PARENT_DIR/"answer_model.md","r",encoding="utf-8") as f:
    answer=f.read()
expansion_model=ChatGroq(model=expansion.strip(),temperature=0)
answer_model=ChatGroq(model=answer.strip(),temperature=0)
