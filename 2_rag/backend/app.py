from fastapi import FastAPI 
from parsers import add_pdfs,add_docxs,add_documents
from show_docs import show_docs
from delete_docs import delete_by_id,delete_all  
app=FastAPI()

#Here are my get endpoints
@app.get("/health")
def health_check():
    return {"Running":"True"}
@app.get("/show_docs")
def list_docs():
    return show_docs()
#Here are my post endpoints:
@app.post("/add_docxs")
def ingest_docx():
    return add_docxs()
@app.post("/add_pdfs")
def ingest_pdfs():
    return add_pdfs()
@app.post("/add_documents")
def ingest_documents():
    return add_documents()
#Here are my delete endpoints:
@app.delete("/delete_all")
def delete_db_docs():
    return delete_all()
@app.delete("/delete/{document_id}")
def delete_doc_by_id(document_id:str):
    return delete_by_id(document_id)
#Here is my point endpoint:
@app.put("/update/{document_id}")
def update_doc_by_id(document_id:str):
    delete_doc_by_id(document_id:str)
    return add_documents()
