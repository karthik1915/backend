from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://karthikeyanj1915:andiamdude@cluster0.wa9qwbd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database_name = "mongodbVSCodePlaygroundDB"
db = client[database_name]
collection_name = "sales"
collection = db[collection_name]


def fetch_data_from_mongodb():
    try:
        # Perform MongoDB query to find all documents in the 'sales' collection
        result = collection.find({})

        # Print the retrieved documents
        for document in result:
            print(document)

    except Exception as e:
        print(f"Error fetching data from MongoDB: {e}")

    finally:
        # Close the MongoDB client connection
        client.close()
        print("Connection closed")


# Fetch and print data from MongoDB
fetch_data_from_mongodb()
