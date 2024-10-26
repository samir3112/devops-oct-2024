# Flask is light weight web application framework
# Flask-RESTful is an extension for Flask
# that adds support for quickly building REST (REpresentational State Transfer) APIs
# Easy to get started with REST API (lacks advanced functionality from full-fledged framework like Django)

# virtualenv avoids the need to install Python packages globally. 
# When a virtualenv is active, pip will install packages within the environment
# which flask (this command gives you flask as global package)

# perform these steps on VSC terminal to install venv

# rm -rf venv
# sudo apt install python3.11-venv
# python3.11 -m venv .venv
# python3 -m pip install --upgrade pip
# source .venv/bin/activate
# you should see (.venv) prepended on VSC terminal

# pip install --upgrade pip
# pip install -r requirements.txt
# which flask (this time it will give path from local environment, which is .venv)

# Ctrl + Shift + P
# Python: Select interpreter
# .venv/bin/python3.11

# if you want to come out of .vnev on ubuntu cli
# deactivate

# import flask

from flask import Flask, request
import json


# import might show error
# ctrl shift P -> Select interpreter -> Enter Interpreter Path  -> Find -> current foler/.venv/bin/python3.11
# create  flash app

app = Flask(__name__)


# create get greeting api and return message and http status code
# define route at which this API would be called


# run python app  with flask run
# Over browser http://localhost:5000/<path>

# running flask app  on other port
# flask run -p 3000

# Or

# if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=3000)

# and run app as python3 app.py

# return dictionary


# return content of json file
# What is JSON
# first read content of json file and convert that to json via json.load() method

with open("../data/fruits_data.json", "r+") as json_file:
    json_data = json.load(json_file)


# update ../data/fruits_data.json
# {"id":6,"fruitName":"Alovera","from":"Tamilnadu","nutrients":"Vitamin B, Vitamin K","price":"200.50","organic":true,"description":"An avocado is a bright green fruit with a large pit and dark leathery skin. They're also known as alligator pears or butter fruit. Avocados are a favorite of the produce section. They're the go-to ingredient for guacamole dips."}

# take user supplied data from request as request.get_json()
# append to json_data (which is obtained from json.load() method
# dump data to same file by with open in w+ mode and using json.dump(json_data, f) method
