from vectorstore import collection  


def show_docs(): 
    docs=[doc for doc in collection.find({},{"_id":0})]
    return docs
