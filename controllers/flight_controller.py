from flask import Blueprint, jsonify, request
from models.flight_model import Flight
from utils.fetch_data import fetch_data
from config import SCHEDULES_URL, DELAYS_URL

flight_bp = Blueprint('flight_bp', __name__)

@flight_bp.route('/get_flight_info', methods=['GET'])
def get_flight_info():
    destination = request.args.get('destination')
    airlines = request.args.getlist('airlines')

    flight_data = fetch_data(SCHEDULES_URL)
    if not flight_data:
        return jsonify({'error': 'Failed to fetch flight schedules data from external API'}), 500

    # Process flight data
    flights_info = Flight.process_flight_data(flight_data, destination, airlines)

    # Now fetch delay data
    delay_data = fetch_data(DELAYS_URL)
    if not delay_data:
        return jsonify({'error': 'Failed to fetch flight delays data from external API'}), 500

    # Add delay info to flights
    Flight.add_delays_to_flights(flights_info, delay_data)

    return jsonify(flights_info)

