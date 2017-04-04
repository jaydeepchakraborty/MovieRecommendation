#reverse

import glob
import os
# import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.movie_database
ratingsCollection = db.ratings_collection


path = '/home/local/ASUAD/jchakra1/Downloads/download/training_set'
db.ratingsCollection.drop();
for filename in glob.glob(os.path.join(path, '*.txt')):
    bulk = db.ratingsCollection.initialize_ordered_bulk_op()
    with open(filename) as f:
        movId = int(f.readline().split(':')[0])
        ratingList = []
        for line in f:
            (uid, rating, date) = line.split(',')
            # Insert movId, rating intp uid tuple
            ratingList.append({
                "movie": movId,
                "uid": uid, 
                "rating": rating,
                "date": date
            });
            
#             pprint.pprint(ratingList)
            
        for i in range(len(ratingList)):
            bulk.find({"userid": ratingList[i]["uid"]}).upsert().update({"$setOnInsert": {"userid": ratingList[i]["uid"],"ratings":[]}});
            bulk.find({"userid": ratingList[i]["uid"]}).update({
                "$push": {
                    "ratings": {
                        "movie": ratingList[i]["movie"],
                        "rating": ratingList[i]["rating"],
                        "date": ratingList[i]["date"]
                        }
                }
            });
             
        bulk.execute()
   
    print(filename)