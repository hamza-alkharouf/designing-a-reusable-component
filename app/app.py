from flask import Flask, request, jsonify
import requests

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
 
@app.route("/api")
def job():
    session = request.args.get('session')
    job = request.args.get('job')
    res = requests.get(f"http://localhost:5000/api?session={session}&job={job}")
    return str(res.text)

@app.route("/api/active")
def active():
    res = requests.get(f"http://localhost:5000/api/active")
    return str(res.text)
 

if __name__ == '__main__':
    app.run(port=4000,debug=True)