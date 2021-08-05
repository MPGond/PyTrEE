import pymongo
from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")
mydb=myclient["mpd"]

print(myclient.list_database_names())
print(mydb.list_collection_names())
mycol=mydb["book"]
#x=mycol.find()
for x in mycol.find():
 print(x)



