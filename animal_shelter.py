import json
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:37712/AAC' % (username, password))
        self.database = self.client['AAC']
    
    # Method to implement the C in CRUD
    def create(self, data):
        # Checks to see if the data is null or empty and returns false in either case
        if data is not None:
            if data:
                # Inserts data inforamtion into animals database
                self.database.animals.insert_one(data)
                return True
        else:
            return False
        
    # Method to implement the R in CRUD
    def read(self, data = None):
        # Checks to see if the data is null or empty and returns exception in either case
        if data is not None:
            if data:
                # Assigns variable with the found data
                data = self.database.animals.find(data,{"_id":False})
        else:
            data = self.database.animals.find({},{"_id":False})
        
        return data 
        
    # Method to implement the U in CRUD
    def update(self, data, updatedData):
        # Checks to see if the data is null or empty and returns exception in either case
        if data is not None:
            # Updates only new data and will not erase fields with no new data
            update = self.database.animals.update_many(data, {"$set": updatedData})
            # Prints amount of documents modified
            confirmation = ("Documents updated: " + json.dumps(update.modified_count))
            return confirmation
        else:
            exception = "Nothing to update, because search parameter is empty"
            return exception
    
    # Method to implement the D in CRUD
    def delete(self, data):
        # Checks to see if the data is null or empty and returns exception in either case
        if data is not None:
            if data:
                deleted = self.database.animals.delete_many(data)
                # Prints amount of documents deleted
                confirmation = ("Documents deleted: " + json.dumps(deleted.deleted_count))
                return confirmation
        else:
            exception = "Nothing to delete, because search parameter is empty"
            return exception
