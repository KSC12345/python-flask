from flask import Flask
from config import load_config

envConfig = load_config()
def create_app():
    app = Flask(__name__)

    # Register blueprints (if any)
    # from .blueprints.example import example_bp
    # app.register_blueprint(example_bp)

    return app