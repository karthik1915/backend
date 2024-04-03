import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv

CONNECTION_STRING = os.getenv('CONNECTION_STRING')


def ContactMessage(data):
    client = MongoClient(CONNECTION_STRING)
    db = client['portfolio']
    collection = db['contact_messages']

    if (collection.insert_one(data)):
        return True
    else:
        return False
