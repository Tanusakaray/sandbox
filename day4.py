from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from pymongo import MongoClient
import json
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

def abort(filter):
    if filter not in find:
        abort(404, message="Plant doesn't exist")

def find(filter):
    client = MongoClient("mongodb+srv://tsakaray:Laddercar33@cluster0.56qnius.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    try:
        conn = MongoClient()
        print("Connected successfully!!!")
    except:  
        print("Could not connect to MongoDB") 
  

    collection = db.PlantDieaseaseMapping 
    found = collection.find_one({"PlantType" : filter})
    return json.loads(dumps(found))



class PlantMapping(Resource):
    def get(self, filter):
        return find(filter)

    """def put(self, filter):
        args = parser.parse_args()
        plant = {"PlantType" : args["PlantType"],"DiseaseName" : args["DiseaseName"], "DiseaseDetails": args["DiseaseDetails"], "TreatmentOption" : args["TreatmentOption"], "TreatmentDetails" : args["TreatmentDetails"]}
        find[filter] = plant
        return plant, 201"""

    """def delete(self, filter):
        abort(filter)
        del find[filter]
        return "", 204"""

api.add_resource(PlantMapping, '/find/<string:filter>')
"""api.add_resource(PlantMapping, '/put/<string:filter>')"""
if __name__ == '__main__':
    app.run(debug=True)
