# coding: utf-8
import os
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    SITE_DOMAIN = "http://localhost:8080"
    port=5001
    url = "https://jsonplaceholder.typicode.com/users/1"
    #MONGO_URI="mongodb://localhost:27017/flaskdb"
    MONGO_URI="mongodb://localhost:27018,localhost:27019,localhost:27020/?replicaSet=s0"    
    MONGO_REPLICA=True