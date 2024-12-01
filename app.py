from flask import Flask,jsonify
from config import load_config
from src.routes.init import api_blueprint
from src.routes.user import user_blueprint
from src.routes.service import service_blueprint
from flasgger import Swagger
#from swaggger_config import swager_init_config
import os

envConfig = load_config()
def create_app():
    app = Flask(__name__)

    # Configuring Swagger
    app.config['SWAGGER'] = {
        'title': 'Sample Python Flask API',
        'description':'This is a sample API with Swagger documentation',
        'uiversion': 3
    }
    if os.environ.get('ENV') != 'PROD':
      swagger = Swagger(app)

    # Register blueprints (if any)
    # from .blueprints.example import example_bp
    # app.register_blueprint(example_bp)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(user_blueprint, url_prefix='/api/user')
    app.register_blueprint(service_blueprint, url_prefix='/api/service')

    # Custom error handler for 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": error.description or "Resource not found"}), 404
    
      # Custom error handler for 400
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": error.description or "Bad request"}), 400
    
      # Custom error handler for 500
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": error.description or "Bad request"}), 500

    return app