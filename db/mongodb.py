import pymongo
from flask_mongoengine import MongoEngine

client = pymongo.MongoClient('localhost', 27017)

db = MongoEngine()