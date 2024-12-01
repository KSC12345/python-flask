from flask import Blueprint,jsonify,abort,request
from src.services.thirdpartyapi import get_service_data

service_blueprint = Blueprint('service', __name__)

# Add routes to the blueprint
@service_blueprint.route('', methods=['GET'])
def callService():
    return jsonify(get_service_data())