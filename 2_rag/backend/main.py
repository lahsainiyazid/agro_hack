from fastapi import FastAPI,File,UploadFile 
from schemas import QuestionRequest 
from parsers import upload_documents 
from show_docs import show_docs 
from delete_docs import delete_by_id,delete_all 
from retrieval import ask_rag_question 
from typing import List 

app=FastAPI()
@app.get("/health")
def health_check():
    return {"Running":"True"}
@app.get("/show_docs")
def list_docs():
    return show_docs()
@app.post("/ask_rag_question")
def ask_question(request:QuestionRequest):
    return ask_rag_question(request)
@app.post("/upload_docs")
async def upload_docs(files:List[UploadFile]=File(...)):
    return await upload_documents(files)
@app.put("/update/{document_id}")
async def update_doc_by_id(document_id:str,files:List[UploadFile]=File(...)):
    delete_by_id(document_id)
    return await upload_documents(files)
@app.delete("/delete_all")
def delete_all_docs():
    return delete_all()
@app.delete("/delete/{document_id}")
def delete_doc_by_id(document_id:str):
    return delete_by_id(document_id)
