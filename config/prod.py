# coding: utf-8
import os
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    SITE_DOMAIN = "http://localhost:8080"
    port=5000
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'your_database',
        'host': 'localhost',
        'port': 27017
    }