from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader 
from text_splitters import text_splitter
from embedding_models import embeddings,reranker 
from vectorstore import vector_store
from pathlib import Path
from itertools import chain 

def add_pdfs():
    path=Path(input("Enter the path to the folder containing your pdfs").strip())
    for file in path.glob("*.pdf"):
        loader=PyPDFLoader(str(file))
        raw_docs=loader.load()
        docs=text_splitter.split_documents(raw_docs)
        for (i,doc ) in enumerate (docs):
            doc.metadata['source']=str(file.name)
            doc.metadata['id']=f"{file.stem}_{i}"
        vector_store.add_documents(documents=docs)
    print("New documents added to mongodb database!")

def add_docxs():
    path=Path(input("Enter the path to the folder containing your docx documents").strip())
    for file in path.glob("*.docx"):
        loader=Docx2txtLoader(str(file))
        raw_docs=loader.load()
        docs=text_splitter.split_documents(raw_docs)
        for (i,doc) in enumerate (docs):
            doc.metadata['source']=str(file.name)
            doc.metadata['id']=f"{file.stem}_{i}"
        vector_store.add_documents(documents=docs)
    print("New word documents added to mongodb database!")

def add_documents():
    path=Path(input("Enter the path to your documents!").strip())
    for file in chain(path.glob("*.pdf"),path.glob("*.docx")):
        if file.suffix.lower()==".pdf":
            loader=PyPDFLoader(str(file))
            raw_docs=loader.load()
            docs=text_splitter.split_documents(raw_docs)
            for (i,doc) in enumerate (docs):
                doc.metadata['source']=str(file.name)
                doc.metadata['id']=f"{file.stem}_{i}"
            vector_store.add_documents(documents=docs)
        if file.suffix.lower()==".docx":
            loader=Docx2txtLoader(str(file))
            raw_docs=loader.load()
            docs=text_splitter.split_documents(raw_docs)
            for (i,doc) in enumerate(docs):
                doc.metadata['source']=str(file.name)
                doc.metadata['id']=f"{file.stem}_{i}"
            vector_store.add_documents(documents=docs)
    print("New docx/pdf documents added to the mongodb database!")




