from flask import request, jsonify

def validate_request():
    destination = request.args.get('destination')
    if destination and len(destination) != 3:
        return jsonify({'error': 'Destination airport code must be exactly 3 characters long'}), 400
