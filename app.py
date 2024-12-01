from flask import Flask,jsonify
from config import load_config
from src.routes.init import api_blueprint
from src.routes.user import user_blueprint

envConfig = load_config()
def create_app():
    app = Flask(__name__)

    # Register blueprints (if any)
    # from .blueprints.example import example_bp
    # app.register_blueprint(example_bp)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(user_blueprint, url_prefix='/api/user')

    # Custom error handler for 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": error.description or "Resource not found"}), 404
    
      # Custom error handler for 400
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": error.description or "Bad request"}), 400

    return app