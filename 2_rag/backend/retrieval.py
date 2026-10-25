from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from schemas import QuestionRequest
from models.prompts.prompts import expansion_prompt,answer_prompt
from models.models import expansion_model,answer_model 
from vectorstore import vector_store,collection,dense
from embedding_models import embeddings 

def ask_rag_question(request:QuestionRequest):
    expansion_query=expansion_model.invoke([expansion_prompt,Question]).content.strip()
    documents=[]
    try :
        cursor=collection.find_all({})
        for item in cursor:
            documents.append(Document(page_content=item.get("text",""),metadata={"source":item,get("source",""),"id":item.get("id","")}))
    except Exception as e:
        print(f"Error while loading chunks {e}")
    if documents:
        bm25=BM25Retriever.from_documents(documents)
        bm25.k=5
        hybrid=EnsembleRetriever(retrievers=[bm25,dense],weights=[0.6,0.4])
        results=hybrid.invoke(expansion_query)
        pairs=[(request.question,doc.page_content) for doc in hybrid.invoke(expansion_prompt)]
        scores=reranker.predict(pairs)
        ranked_docs=[doc for _,doc in sorted(zip(scores,result),key=lambda x:x[0],reverse=True)]
        final_docs=ranked_docs[:5] 
        context="\n\n".join(doc.page_content for doc in final_docs)
        answer=answer_model.invoke([answer_prompt,context])
        return answer
    else:
        bm25=None 
        dense=None 
        hybrid=None
        return {""}



