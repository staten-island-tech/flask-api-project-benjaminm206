from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https:")