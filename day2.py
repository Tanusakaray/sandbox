from pymongo import MongoClient

# connection string 
client = MongoClient("mongodb+srv://lsakaray:Laddercar33@cluster0.56qnius.mongodb.net/?retryWrites=true&w=majority")
db = client.test


try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  

collection = db.PlantDieaseaseMapping 

rec1 = {
    "PlantType" : "Strawberry",
    "PlantImage" : "",
    "DiseaseName" : "Spider Mites",
    "DiseaseDetails" : "They are little arachnids that are less than one mm long",
    "TreatmentOption" : "Use sticky traps",
    "TreatmentDetails" : "when you hang these around the room, you can trap the pets and that makes it easy to identify them (and of course, it takes them out of the game). Blue stick cards are good for thrips. Yellow cards attract fungus gnats and whiteflies. Tip: make sure some cards are at the soil/medium level of your plants—where fungus gnats congregate."
}

rec_id1 = collection.insert_one(rec1)

cursor = collection.find()
for record in cursor:
    print(record)

def insert():
    PlantType = input("Enter Plant Type")
    DiseaseName = input("Enter Disease Name")
    DiseaseDetails = input("Enter Plant Type")
    TreatmentOption =
    TreatmentDetails =
    rec_id1 = collection.insert_one(rec1)

def update():

def delete():

def find():
    
# input from user 
user = int(input("What operation do you want? "))
if user == 1:

