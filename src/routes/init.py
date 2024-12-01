from flask import Blueprint,jsonify

api_blueprint = Blueprint('api', __name__)

# Add routes to the blueprint
@api_blueprint.route('', methods=['GET'])
def init():
    return jsonify({"message": "This is init"})