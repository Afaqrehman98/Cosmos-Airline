import uuid

class Flight:
    @staticmethod
    def process_flight_data(flight_data, delay_data, destination, airlines):
        flights_info = []
        seen_flights = set()

        flights = flight_data.get('FlightStatusResource', {}).get('Flights', {}).get('Flight', [])
        for flight in flights:
            if not Flight.is_valid_flight(flight, destination, airlines, seen_flights):
                continue

            flight_id = str(uuid.uuid4())
            flight_code = f"{flight['MarketingCarrier']['AirlineID']}{flight['MarketingCarrier']['FlightNumber']}"
            delays_info = Flight.get_delays_for_flight(flight_code, delay_data)

            flights_info.append({
                'id': flight_id,
                'flight_number': flight['MarketingCarrier'].get('FlightNumber', 'N/A'),
                'airline': flight['MarketingCarrier'].get('AirlineID', 'N/A'),
                'origin': flight['Departure'].get('AirportCode', 'N/A'),
                'destination': flight['Arrival'].get('AirportCode', 'N/A'),
                'scheduled_departure_at': flight['Departure'].get('ScheduledTimeLocal', {}).get('DateTime', 'N/A'),
                'actual_departure_at': flight['Departure'].get('ActualTimeLocal', {}).get('DateTime', 'N/A'),
                'delays': delays_info if delays_info else [{'code': 'N/A', 'time_minutes': 'N/A', 'description': 'N/A'}]
            })

            seen_flights.add(flight_code)

        for flight in flights_info:
            flight['delays'] = sorted(flight['delays'], key=lambda x: x['code'])

        return flights_info

    @staticmethod
    def is_valid_flight(flight, destination, airlines, seen_flights):
        arrival = flight.get('Arrival', {})
        marketing_carrier = flight.get('MarketingCarrier', {})
        flight_code = f"{marketing_carrier.get('AirlineID', '')}{marketing_carrier.get('FlightNumber', '')}"

        return (not destination or arrival.get('AirportCode') == destination) and \
               (not airlines or marketing_carrier.get('AirlineID') in airlines) and \
               flight_code not in seen_flights

    @staticmethod
    def get_delays_for_flight(flight_code, delay_data):
        delays_info = []

        for delay in delay_data:
            if Flight.matching_flight_code(delay, flight_code):
                delays_info.extend(Flight.extract_delays(delay))

        return delays_info

    @staticmethod
    def matching_flight_code(delay, flight_code):
        operating_flight = delay.get('Flight', {}).get('OperatingFlight', {})
        current_flight_code = f"{operating_flight.get('Airline', '')}{operating_flight.get('Number', '')}"
        return current_flight_code == flight_code

    @staticmethod
    def extract_delays(delay):
        delays_info = []
        flight_legs = delay.get('FlightLegs', [])

        for flight_leg in flight_legs:
            departure_leg = flight_leg.get('Departure')
            if departure_leg:
                delays_info.extend(Flight.extract_delay_codes(departure_leg))

        return delays_info

    @staticmethod
    def extract_delay_codes(departure_leg):
        delays = departure_leg.get('Delay', {})
        delays_info = []

        for key, delay_code_obj in delays.items():
            if not delay_code_obj: 
                continue

            delay_code = delay_code_obj.get('Code', 'N/A')
            if delay_code != 'N/A':
                delays_info.append({
                    'code': delay_code,
                    'time_minutes': delay_code_obj.get('DelayTime', 'N/A'),
                    'description': delay_code_obj.get('Description', 'N/A') if delay_code_obj.get('Description') else 'N/A'
                })

        return delays_info
