from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def api_grab_key():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            return request.json["imgUrl"]
        else:
            return "Request must be in JSON"
    if request.method == 'GET':
        return "Hello World! GET request"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
