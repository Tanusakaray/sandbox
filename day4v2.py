from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import json
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)


def connection():
    client = MongoClient(
        "mongodb+srv://tsakaray:Laddercar33@cluster0.56qnius.mongodb.net/?retryWrites=true&w=majority")
    db = client.test

    try:
        conn = MongoClient()
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    collection = db.PlantDieaseaseMapping
    return collection


@app.route('/', methods=['GET'])
def get():
    mongo_collection = connection()
    found = mongo_collection.find_one({"PlantType": "Strawberry"})
    return json.loads(dumps(found))


@app.route('/', methods=['DELETE'])
def delete():
    mongo_collection = connection()
    found = mongo_collection.find_one_and_delete(
        {"PlantType": "Strawberry"})
    return json.loads(dumps(found))

@app.route('/', methods=['PUT'])
def put():
    mongo_collection = connection()
    found = mongo_collection.find_one_and_update({"PlantType": "Strawberry"}, {
        "$set": {"DiseaseName": "Orange", "DiseaseDetails": "Lemon"}})
    return json.loads(dumps(found))

@app.route('/', methods=['POST'])
def post():
    mongo_collection = connection()
    dict1 = {"PlantType": "Pig", "DiseaseName": "Crow", "DiseaseDetails": "Moose",
             "TreatmentOption": "Maze", "TreatmentDetails": "Farm"}
    found = mongo_collection.insert_one(dict1)
    return json.loads(dumps("Inserted Successfully"))


if __name__ == '__main__':
    app.run(debug=True)
