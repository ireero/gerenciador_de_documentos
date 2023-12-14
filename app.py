from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flask_bootstrap import Bootstrap5
import os

MONGO_PWD = os.getenv('MONGO_PWD')

connection_string = f'mongodb+srv://ireerovsky:{MONGO_PWD}@cluster0.bezpqbb.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(connection_string, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)
bootstrap = Bootstrap5(app)

from calls import calls as calls_blueprint

app.register_blueprint(calls_blueprint)

from navigation import navigation as navigation_blueprint

app.register_blueprint(navigation_blueprint)

with app.app_context():
    if __name__ == '__main__':
        app.run(debug=False)