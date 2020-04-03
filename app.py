from flask import Flask, Response, jsonify, request, render_template
from flask_assistant import Assistant, tell
from flask_cors import CORS
from pprint import pprint
import json, jsonify, requests
import GetSnap

app = Flask(__name__)
cors = CORS(app)
assist = Assistant(app, route='/google')

@app.route("/", methods=['GET'])
def main():
    tags = GetSnap.tags
    return str(tags)

@assist.action('tv-watch')
def google_tv_watch():
    return tell(print(GetSnap.tags))

if __name__ == '__main__':
    app.run(threaded=True, port=5000)