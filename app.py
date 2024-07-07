from flask import Flask, jsonify, request
import requests
import uuid
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for the API URLs
SCHEDULES_URL = 'https://challenge.usecosmos.cloud/flight_schedules.json'
DELAYS_URL = 'https://challenge.usecosmos.cloud/flight_delays.json'

def fetch_data(url):
    """Fetch data from a given URL and return the JSON response."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError on bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from {url}: {e}")
        return None

def get_delays_for_flight(flight_code, delay_data):
    """Fetch delay information for a specific flight from the delay dataset."""
    delays_info = []

    for delay in delay_data:
        operating_flight = delay.get('Flight', {}).get('OperatingFlight', {})
        current_flight_code = f"{operating_flight.get('Airline', '')}{operating_flight.get('Number', '')}"

        if current_flight_code == flight_code:
            flight_legs = delay.get('FlightLegs', [])
            if flight_legs:
                for flight_leg in flight_legs:
                    departure_leg = flight_leg.get('Departure')
                    if departure_leg:
                        for code_num in range(1, 5):
                            delay_code_obj = departure_leg.get('Delay', {}).get(f'Code{code_num}')
                            if delay_code_obj:
                                delay_code = delay_code_obj.get('Code', 'N/A')
                                delay_time = delay_code_obj.get('DelayTime', 'N/A')
                                delay_desc = delay_code_obj.get('Description', 'N/A')
                                if delay_code != 'N/A':
                                    delays_info.append({
                                        'code': delay_code,
                                        'time_minutes': delay_time,
                                        'description': delay_desc if delay_desc else 'N/A'
                                    })
    return delays_info

@app.route('/get_flight_info', methods=['GET'])
def get_flight_info():
    destination = request.args.get('destination')
    airlines = request.args.getlist('airlines')

    flight_data = fetch_data(SCHEDULES_URL)
    if not flight_data:
        return jsonify({'error': 'Failed to fetch flight schedules data from external API'}), 500

    delay_data = fetch_data(DELAYS_URL)
    if not delay_data:
        return jsonify({'error': 'Failed to fetch flight delays data from external API'}), 500

    flights_info = []
    seen_flights = set()

    for flight in flight_data.get('FlightStatusResource', {}).get('Flights', {}).get('Flight', []):
        departure = flight.get('Departure', {})
        arrival = flight.get('Arrival', {})
        marketing_carrier = flight.get('MarketingCarrier', {})

        flight_code = f"{marketing_carrier.get('AirlineID', '')}{marketing_carrier.get('FlightNumber', '')}"
        
        if (not destination or arrival.get('AirportCode') == destination) and \
           (not airlines or marketing_carrier.get('AirlineID') in airlines) and \
           flight_code not in seen_flights:

            flight_id = str(uuid.uuid4())
            delays_info = get_delays_for_flight(flight_code, delay_data)

            flights_info.append({
                'id': flight_id,
                'flight_number': marketing_carrier.get('FlightNumber', 'N/A'),
                'airline': marketing_carrier.get('AirlineID', 'N/A'),
                'origin': departure.get('AirportCode', 'N/A'),
                'destination': arrival.get('AirportCode', 'N/A'),
                'scheduled_departure_at': departure.get('ScheduledTimeLocal', {}).get('DateTime', 'N/A'),
                'actual_departure_at': departure.get('ActualTimeLocal', {}).get('DateTime', 'N/A'),
                'delays': delays_info if delays_info else [{'code': 'N/A', 'time_minutes': 'N/A', 'description': 'N/A'}]
            })

            seen_flights.add(flight_code)

    for flight in flights_info:
        flight['delays'] = sorted(flight['delays'], key=lambda x: x['code'])

    return jsonify(flights_info)

if __name__ == '__main__':
    app.run(debug=True)
