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


@app.route('/find', methods=['GET'])
def get():
    args = request.args
    print(args)
    mongo_collection = connection()
    filter = args.get("filter")
    found = mongo_collection.find_one({"PlantType": filter})
    return json.loads(dumps(found))


@app.route('/remove', methods=['DELETE'])
def delete():
    args = request.args
    mongo_collection = connection()
    filter = args.get("filter")
    found = mongo_collection.find_one_and_delete({"PlantType": filter})
    return json.loads(dumps(found))

@app.route('/update', methods=['PUT'])
def put():
    args = request.args
    print(request.data)
    record = json.loads(request.data)
    mongo_collection = connection()
    filter = args.get("filter")
    found = mongo_collection.find_one_and_update({"PlantType": filter}, {"$set": record})
    return json.loads(dumps(found))

@app.route('/insert', methods=['POST'])
def post():
    print(request.data)
    record = json.loads(request.data)
    mongo_collection = connection() 
    found = mongo_collection.insert_one(record)
    return json.loads(dumps("Inserted Successfully"))


if __name__ == '__main__':
    app.run(debug=True)