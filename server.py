
from flask import Flask
import flask_restful
from pymongo import MongoClient
from flask import make_response
from bson.json_util import dumps
from flask_restful import Api, Resource
#import resources


app = Flask(__name__)
api = Api(app)
uri = "mongodb://inegi:rsF7vS5QFZmUCLTHNo7sEYTN3lOxVkHJSH6Vf3xlSGbj8hXzM3hGxZHNxTe9Fny296ya4BgjnSetDZyrj4b8yA==@inegi.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
db = MongoClient(uri)
mongo = db.inegi




class Root(Resource):
    def get(self):
        res = mongo.denue.find().limit(1)
        resp = dumps(res,indent=1, ensure_ascii=False).encode('utf8')
        return resp
    

api.add_resource(Root, '/')        

if __name__ == "__main__":
	app.run()
