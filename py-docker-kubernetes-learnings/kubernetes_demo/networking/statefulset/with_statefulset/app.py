from flask import Flask, request

# connection string to write
from mongo_pass import mongo_connection_string_write
# connection string to read
from mongo_pass import mongo_connection_string_read
from pymongo import MongoClient

app = Flask(__name__)
client_write = MongoClient(mongo_connection_string_write)
client_read = MongoClient(mongo_connection_string_read)

# Database  and Table for write client
db_write = client_write.get_database('fruits_db') 
fruits_coll_write = db_write.fruits_coll


# Database  and Table for read client
db_read = client_read.get_database('fruits_db') 
fruits_coll_read = db_read.fruits_coll


# api writes to pod0
@app.post("/mongodb-0/api/v1/fruits")
def create_fruits():
    request_data = request.get_json()
    fruits_coll_write.insert_one(request_data) 
    return {"message":"ok"}, 201

# api writes to pod0
@app.get("/mongodb-0/api/v1/fruits")
def get_all_fruits_mongodb_0(): 
    query_results = fruits_coll_write.find({}, {'_id': False})
    return list(query_results), 200

# api writes to pod1
@app.get("/mongodb-1/api/v1/fruits")
def get_all_fruits_mongodb_1(): 
    query_results = fruits_coll_read.find({}, {'_id': False})
    return list(query_results), 200