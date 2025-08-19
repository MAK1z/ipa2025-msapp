from pymongo import MongoClient
client = MongoClient("mongodb://mongo:27017/")
mydb = client["ipa2025"]
mycol = mydb["routers"]
print("start")
print(client.list_database_names())
print(mydb.list_collection_names())
print("end")