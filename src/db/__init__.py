from pymongo import MongoClient
from flask import g
from config import load_config
envConfig = load_config()

def get_db():
    if 'db' not in g:
        g.db = MongoClient(envConfig.MONGO_URI)
    return g.db.flaskdb

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()