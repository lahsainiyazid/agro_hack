from vectorstore import collection 

def delete_by_id(document_id):
    result=collection.delete_one({"_id":ObjectId(document_id)})
    if result.deleted_count>0:
        print("Successfuly deleted doc")
    else:
        print("No documents were deleted")


def delete_all():
    collection.delete_many({})
    print("All documents were deleted")


