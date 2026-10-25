from models.prompts.prompts import expansion_prompt,answer_prompt
from models.models import expansion_model,answer_model 
from vectorstore import vector_store,collection
from embedding_models import embeddings 

print(expansion_prompt)
print(answer_prompt)

def ask_rag_question(Question:str):
    expansion_prompt=expansion_model.invoke([expansion_prompt,Question]).content.strip()
    documents=[]
    try :
        cursor=collection.find_all({})
        for item in cursor:
            documents.append(Document(page_content=item.get("text",""),metadata={"source":item,get("source",""),"id":item.get("id","")}))
    except Exception as e:
        print(f"Error while loading chunks {e}")

