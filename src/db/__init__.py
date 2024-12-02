from pymongo import MongoClient
from flask import g
from config import load_config
envConfig = load_config()
dbCon = {}
def get_db():
    return get_connection().flaskdb

def get_connection():
    if 'db' not in dbCon:
        dbCon["db"] = MongoClient(envConfig.MONGO_URI)
    return dbCon["db"]


def close_db(e=None):
    db = dbCon.pop('db', None)
    if db is not None:
        db.close()