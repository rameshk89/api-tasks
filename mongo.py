"""
Mongodb client for python
"""
from enum import Enum
from pymongo import MongoClient

class Table(Enum):
    """  List of collections """
    users = "users"
    posts = "posts"

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONN_URL = "mongodb+srv://rickirathi:ricki@cluster0.n8scg.mongodb.net"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(
    CONN_URL,
    tls=True,
    tlsCAFile='/opt/python/3.10.4/lib/python3.10/site-packages/certifi/cacert.pem')

def get_database():
    """
    Create a py db connection
    """
    return client['db']

def insert_document(document, collection: Table):
    """
    Insert one
    """
    client = get_database()
    coll_ref = client[collection.value]
    coll_ref.insert_one(document)

def insert_documents(docs, collection: Table):
    """
    Insert many
    """
    client = get_database()
    coll_ref = client[collection.value]
    coll_ref.insert_many(docs)

def get_records(collection: Table):
    """
    read many
    """
    client = get_database()
    coll_ref = client[collection.value]
    docs = coll_ref.find()
    return docs

# Testing the code
import datetime

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
insert_document(post, Table.posts)
record = get_records(Table.posts)
print(record)