# CS 340 Project One CRUD module for the Grazioso Salvare project

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username='aacuser', password='AACuser2026'):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is set up to use the aac
        # database and the animals collection. The username and password
        # can be now passed in from Module Five
        # Dash dashboard login form.
        # Connection Variables

        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as error:
                print("Create operation failed:", error)
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        """Find documents in the animals collection."""

        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except PyMongoError as error:
                print("Read operation failed:", error)
                return []
        else:
            return []

    # Update method to implement the U in CRUD.
    def update(self, query, new_values):
        """Update one document in the animals collection."""

        if (
            query is not None
            and isinstance(query, dict)
            and new_values is not None
            and isinstance(new_values, dict)
        ):
            try:
                result = self.collection.update_one(query, new_values)
                return result.modified_count
            except PyMongoError as error:
                print("Update operation failed:", error)
                return 0
        else:
            return 0

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete one document from the animals collection."""

        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_one(query)
                return result.deleted_count
            except PyMongoError as error:
                print("Delete operation failed:", error)
                return 0
        else:
            return 0
