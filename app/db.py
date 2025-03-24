from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client['chat_app_db']

users_collection = db['users']
messages_collection = db['messages']
