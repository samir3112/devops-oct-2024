from flask import Flask, request
import json

app = Flask(__name__)

# read JSON file
# Opening JSON file
with open('./data/fruits_data.json') as json_file:
    fruits_json = json.load(json_file)

@app.get("/api/v1/fruits")
def get_all_fruits():
    print("get_all_fruits() :: entered")
    return fruits_json, 200

@app.get("/api/v1/fruits/<string:fruit_name>")
def get_a_fruit(fruit_name):
    for fruit in fruits_json:
        print(f"get_a_fruit() :: fruit is {fruit}")
        if fruit["fruitName"].lower() == fruit_name.lower():
            return fruit, 200
    return {"message":f"Fruits with name {fruit_name} is not found"}, 401

@app.post("/api/v1/fruits")
def create_a_fruit():
    fruit_from_request = request.get_json()
    print(f"fruit_from_request is {fruit_from_request}")
    id_for_new_fruit = len(fruits_json)
    fruit_from_request["id"] = id_for_new_fruit
    fruits_json.append(fruit_from_request)
    with open('./data/fruits_data.json', 'w') as f:
        json.dump(fruits_json, f)    
    return fruit_from_request, 201
