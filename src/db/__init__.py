from pymongo import MongoClient
from flask import g
from config import load_config
envConfig = load_config()

def get_db():
    return get_connection().flaskdb

def get_connection():
    if 'db' not in g:
        g.db = MongoClient(envConfig.MONGO_URI)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()