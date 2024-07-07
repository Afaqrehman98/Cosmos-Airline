import uuid

class Flight:
    @staticmethod
    def process_flight_data(flight_data, destination, airlines):
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

                flight_info = {
                    'id': flight_id,
                    'flight_number': marketing_carrier.get('FlightNumber', 'N/A'),
                    'airline': marketing_carrier.get('AirlineID', 'N/A'),
                    'origin': departure.get('AirportCode', 'N/A'),
                    'destination': arrival.get('AirportCode', 'N/A'),
                    'scheduled_departure_at': departure.get('ScheduledTimeLocal', {}).get('DateTime', 'N/A'),
                    'actual_departure_at': departure.get('ActualTimeLocal', {}).get('DateTime', 'N/A'),
                    'delays': []
                }

                flights_info.append(flight_info)
                seen_flights.add(flight_code)

        return flights_info

    @staticmethod
    def add_delays_to_flights(flights_info, delay_data):
        flight_map = {f"{flight['airline']}{flight['flight_number']}": flight for flight in flights_info}

        for delay in delay_data:
            operating_flight = delay.get('Flight', {}).get('OperatingFlight', {})
            flight_code = f"{operating_flight.get('Airline', '')}{operating_flight.get('Number', '')}"

            if flight_code in flight_map:
                flight_legs = delay.get('FlightLegs', [])
                if flight_legs:
                    for flight_leg in flight_legs:
                        departure_leg = flight_leg.get('Departure')
                        if departure_leg:
                            for code_num in range(1, 5):
                                delay_code_obj = departure_leg.get('Delay', {}).get(f'Code{code_num}')
                                if delay_code_obj:
                                    delay_info = {
                                        'code': delay_code_obj.get('Code', 'N/A'),
                                        'time_minutes': delay_code_obj.get('DelayTime', 'N/A'),
                                        'description': delay_code_obj.get('Description', 'N/A')
                                    }
                                    flight_map[flight_code]['delays'].append(delay_info)

        for flight in flights_info:
            flight['delays'] = sorted(flight['delays'], key=lambda x: x['code'])
