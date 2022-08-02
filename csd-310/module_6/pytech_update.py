import pymongo
from pymongo import MongoClient 
client=MongoClient("mongodb+srv://admin:admin@cluster0.cnec1ir.mongodb.net/?retryWrites=true&w=majority")
db= client["pytech"]
collection= db["students"]

result= db.collection.update_one({"student_id":1007}), {"$set": {"last_name":"Henry"}}