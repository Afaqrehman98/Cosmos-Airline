from models.flight_model import Flight
from utils.fetch_data import fetch_data
from config import SCHEDULES_URL, DELAYS_URL

def get_flight_info_controller(destination, airlines):
    flight_data = fetch_data(SCHEDULES_URL)
    if not flight_data:
        return {'error': 'Failed to fetch flight schedules data from external API'}, 500

    delay_data = fetch_data(DELAYS_URL)
    if not delay_data:
        return {'error': 'Failed to fetch flight delays data from external API'}, 500

    if isinstance(airlines, str):
        airlines = [airlines]

    flights_info = Flight.process_flight_data(flight_data, delay_data, destination, airlines)
    return flights_info
