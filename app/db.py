from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # Default MongoDB URL
db = client['chat_app_db']

users_collection = db['users']
messages_collection = db['messages']
