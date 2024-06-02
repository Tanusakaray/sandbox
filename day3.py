from pymongo import MongoClient

client = MongoClient("mongodb+srv://tsakaray:Laddercar33@cluster0.56qnius.mongodb.net/?retryWrites=true&w=majority")
db = client.test

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  

collection = db.PlantDieaseaseMapping 

def insert():
    PlantType = input("Enter Plant Type: ")
    DiseaseName = input("Enter Disease Name: ")
    DiseaseDetails = input("Enter Disease Details: ")
    TreatmentOption = input("Enter Treatment Option: ")
    TreatmentDetails = input("Enter Treatment Details: ")
    dict1 = {"PlantType" : PlantType, "DiseaseName" : DiseaseName, "DiseaseDetails": DiseaseDetails, "TreatmentOption" : TreatmentOption, "TreatmentDetails" : TreatmentDetails}
    collection.insert_one(dict1)
    

def find():
    user = input("Enter a Plant Type: ")
    found = collection.find_one({"PlantType" : user})
    print(found)

def update():
    user = input("Enter what Plant Type you want to update?: ")
    updated = collection.find_one({"PlantType" : user})
    user1 = input("Enter the updated Disease Name: ")
    user2 = input("Enter the updated Disease Details: ")
    collection.find_one_and_update({"PlantType" : user}, { "$set" : { "DiseaseName" : user1, "DiseaseDetails" : user2 } })

def delete():
    user = input("Enter the Plant Type that you want to delete? ")
    collection.find_one_and_delete({"PlantType" : user})

def find_all():
    cursor = collection.find()
    for record in cursor:
        print(record)

def main():
    user = 0
    while user != 5:
        print("""
        insert: 1
        find: 2
        update: 3
        delete: 4
        find_all: 5
        """)
        user = int(input("What operation do you want? "))
        if user == 1:
            insert()
        if user == 2:
            find()
        if user == 3:
            update()
        if user == 4:
            delete()
        if user == 5:
            find_all()


main()
