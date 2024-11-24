from flask import Flask
import requests

app = Flask(__name__)


@app.get("/movies")
def get_greetings():
    response = requests.get('https://swapi.dev/api/films')
    return response.json(), 200

