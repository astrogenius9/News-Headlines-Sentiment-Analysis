from pymongo import MongoClient

def get_db():
    # Create a MongoDB client and connect to the database
    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
    db = client['news_sentiment_db']  # Database name
    return db

def insert_data(collection_name, data):
    db = get_db()
    collection = db[collection_name]
    collection.insert_many(data)  # Insert a list of documents (articles)
