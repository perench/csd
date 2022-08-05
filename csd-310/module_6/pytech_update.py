import pymongo
from pymongo import MongoClient 
client= MongoClient("mongodb+srv://admin:admin@cluster0.cnec1ir.mongodb.net/?retryWrites=true&w=majority")
db= client["pytech"]
collection= db["students"]

post1={"_id": 1007, "First Name":"Andrew", "Last Name":"Rench"}
post2={"_id": 1008, "First Name": "Peyton", "Last Name": "Rench"}
post3={"_id": 1009, "First Name": "Alyssa", "Last Name": "Rench"}

#collection.insert_one(post1)

collection.insert_many([post1,post2,post3])

db.sample.update({"_id":"1007"},{"$set":{"Last Name":"Henry"}})