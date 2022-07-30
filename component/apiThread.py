from flask import Flask
from flask_restful import Resource, Api, reqparse

from thread import thread,jobActive
 
app = Flask(__name__)
api = Api(app)
 
parser = reqparse.RequestParser()
parser.add_argument('session', type=int,required=True ,help='enter session', location='args')
parser.add_argument('job', type=str,required=True ,help='enter job', location='args')

class job(Resource):
    def get(self):
        return thread(parser.parse_args())

class activeJob(Resource):
    def get(self):
        return jobActive()
 
api.add_resource(job, '/api')
api.add_resource(activeJob, '/api/active') 
 
 
if __name__ == '__main__':
    app.run(debug=True)