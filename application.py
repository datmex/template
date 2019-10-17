
from flask import Flask, jsonify
import flask_restful
from pymongo import MongoClient
from flask import make_response
from bson.json_util import dumps
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
#import resources

app = Flask(__name__)
api = Api(app)
uri = "mongodb://inegi:rsF7vS5QFZmUCLTHNo7sEYTN3lOxVkHJSH6Vf3xlSGbj8hXzM3hGxZHNxTe9Fny296ya4BgjnSetDZyrj4b8yA==@inegi.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
db = MongoClient(uri)
mongo = db.inegi

app.config['MONGO_URI'] = uri
mongo = PyMongo(app)
mongo = mongo.db['inegi']

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

class Root(Resource):
    def get(self):
        res = mongo.denue.find().limit(1)
        resp = dumps(res,indent=1, ensure_ascii=False).encode('utf8')
        return jsonify(resp)
    
class Hola(Resource):
    def get(self):
        return "Hola mundo!"

api.add_resource(Hola, '/d')
api.add_resource(Root, '/')        

if __name__ == "__main__":
	app.run()
