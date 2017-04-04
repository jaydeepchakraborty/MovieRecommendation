#reverse

import glob
import os
import random
# import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.movie_database
ratingsCollection = db.ratings_collection


def getDataMatrix(userObject):
    userId = userObject["userid"]
    movieIds = [userObject["ratings"][i]["movie"] for i in range(len(userObject["ratings"]))]
    print(movieIds)
    
    # query to get all users with these movieIds
    trainingUsers = db.ratingsCollection.find({
        "ratings.movie": {"$all": movieIds}
    })
    f = open("text.csv", "w")
    f.write("0, " + ", ".join(str(x) for x in movieIds) + "\n")
    for doc in trainingUsers:
        line = doc["userid"] + ", "
        for movie in movieIds:
            for rating in doc["ratings"]:
                if (rating["movie"] == movie):
                    line = line + rating["rating"] + ", "
        line = line[:-2]
        f.write(line+"\n")
    f.close()
    


totalDocuments = db.ratingsCollection.find().count();
print(totalDocuments)
randomIndex = random.randint(1, totalDocuments)
# randomIndex = 16272
# userObj = db.ratingsCollection.find().limit(-1).skip(randomIndex).next()
userObj = db.ratingsCollection.find({"userid": "16272"})[0]
print(userObj)

getDataMatrix(userObj)