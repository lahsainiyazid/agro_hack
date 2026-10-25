from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader 
from text_splitters import text_splitter
from embedding_models import embeddings,reranker 
from vectorstore import vector_store
from pathlib import Path
import tempfile 
from fastapi import File,UploadFile
from itertools import chain 
from typing import List
async def upload_documents(files:List[UploadFile]=File(...)):
    processed_count=0
    for upload_file in files:
        filename=upload_file.filename or ""
        filepath=Path(filename)
        suffix=filepath.suffix.lower() 
        if suffix not in [".pdf",".docx"]:
            continue
        with tempfile.NamedTemporaryFile(delete=False,suffix=suffix) as tmp:
            contents=await upload_file.read()
            tmp.write(contents)
            tmp_path=tmp.name 
        try :
            if suffix==".pdf":
                loader=PyPDFLoader(tmp_path)
            else:
                loader=Docx2txtLoader(tmp_path)
            raw_docs=loader.load()
            docs=text_splitter.split_documents(raw_docs)
            for (i,doc) in enumerate (docs):
                doc.metadata["source"]=filepath.name
                doc.metadata["id"]=f"{filepath.stem}_{i}"
            vector_store.add_documents(documents=docs)
            processed_count+=1
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    return {"message":f"Processed {processed_count} documents to the database"}


