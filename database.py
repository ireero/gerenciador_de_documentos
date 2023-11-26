from pymongo import MongoClient
from app import client

class BaseDeDados:

    def __init__(self) -> None:
        self.db = client['documents_control']
        self.requisitions = self.db.requisitions