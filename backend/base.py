from flask import Flask, request
import ai

api = Flask(__name__)

@api.route('/')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        ai.getfile(file)

api.run()