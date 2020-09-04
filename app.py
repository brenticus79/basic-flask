from flask import Flask
import socket
import json


app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/')
def hello_world():
    return json.dumps({'Host': hostname, 'Message': 'Hello World'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

