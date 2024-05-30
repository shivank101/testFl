from flask import Flask, request
import pickle

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['GET'])
def ping():
    return {"message": "Hi there, I'm working!!"}