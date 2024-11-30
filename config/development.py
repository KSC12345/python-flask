# coding: utf-8
import os
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    SITE_DOMAIN = "http://localhost:8080"
    port=5001
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'your_database',
        'host': 'localhost',
        'port': 27017
    }