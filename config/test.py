# coding: utf-8
import os
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    SITE_DOMAIN = "http://localhost:8080"
    port=5001
    url = "https://jsonplaceholder.typicode.com/users/1"
    # MongoEngine config
    MONGO_URI="mongodb://localhost:27017/flaskdb"