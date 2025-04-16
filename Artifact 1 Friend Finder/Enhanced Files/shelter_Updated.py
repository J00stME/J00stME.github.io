from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, but the aac user is passed from the dashboard
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method for CRUD operations
    def create(self, data):
        if data is not None:
            success = self.database.animals.insert_one(data)  # data should be dictionary
            #returns true or false if create succeeds
            if success.acknowledged:
                return True
            else:
                return False
        else:
            #no data passed to method
            raise Exception("Nothing to save, because data parameter is empty")

# Read method for CRUD operations

    def read(self, query):
        if query:
            #queries DB if query is not null
            search = self.database.animals.find(query, {"_id" : False})
        else:
            #defaults if query is null
            search = self.database.animals.find({}, {"_id" : False})
        return search
    
# Update method for CRUD operations    
    
    def update(self, query, newVals):
        if (query and newVals):
            success = self.database.animals.update_many(query, {"$set" : newVals})
            return success.modified_count
        else:
            #no data passed to method for either query or newvals
            raise Exception("One or more queries not specified")
            
# Delete method for CRUD operations

    def delete(self, query):
        if query:
            #if query exists, will query database, delete any column with key/val pair, return amount deleted
            success = self.database.animals.delete_many(query)
            return success.deleted_count
        else:
            raise Exception("No query made")

            