from flask import Blueprint, jsonify, request
from controllers.flight_controller import get_flight_info_controller
from middlewares.validation_middleware import validate_parameters, validate_destination

flight_bp = Blueprint('flight_bp', __name__)

@flight_bp.route('/get_flight_info', methods=['GET'])
@validate_destination
@validate_parameters
def get_flight_info():
    destination = request.args.get('destination', '').upper()  # Normalize to uppercase
    airlines = [airline.upper() for airline in request.args.getlist('airlines')] 
    flights_info = get_flight_info_controller(destination, airlines)
    return jsonify(flights_info)
