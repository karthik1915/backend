from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://karthikeyanj1915:andiamdude@cluster0.wa9qwbd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


def ContactMessage(data):
    client = MongoClient(CONNECTION_STRING)
    db = client["portfolio"]
    collection = db["contact_messages"]

    if collection.insert_one(data):
        return True
    else:
        return False
