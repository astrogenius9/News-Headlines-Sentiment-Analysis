from pymongo import MongoClient
from bson import ObjectId

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['newsapi_db']
collection = db['articles']

def insert_article(article):
    try:
        result = collection.insert_one(article)  # Insert the article into the collection
        return result
    except Exception as e:
        print(f"Error inserting article: {e}")
        return None
