from flask import Flask,jsonify,request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/get-value')
def get_value():
    val = os.getenv('TEST', 'default_value')
    return jsonify({"env value":val})


if __name__ == "__main__":
     app.run()
