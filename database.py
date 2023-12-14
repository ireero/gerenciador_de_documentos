from pymongo import MongoClient
from app import client

class BaseDeDados:

    def __init__(self) -> None:
        self.db_documents = client['documents_control']
        self.collection_documents = self.db_documents.requisitions
        self.db_users = client['users_control']
        self.collection_users = self.db_users.requisitions
    
    def insert_document(self, document):
        inserted_id = self.collection_documents.insert_one(document).inserted_id
        print(f'Nova documento inserido com sucesso! id: {inserted_id}')
    
    def find_all_documents(self):
        documents = self.collection_documents.find()
        return list(documents)
    
    def count_all_documents(self):
        count = self.collection_documents.count_documents(filter={})
        return count
    
    def get_document_by_id(self, str_document_id):
        from bson.objectid import ObjectId
        _id = ObjectId(str_document_id)
        document = self.collection_documents.find_one({"_id": _id})
        return document