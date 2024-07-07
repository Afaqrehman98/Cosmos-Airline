from flask import request, jsonify
from functools import wraps

def validate_destination(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        destination = request.args.get('destination')
        if destination and len(destination) != 3:
            return jsonify({'error': 'Destination airport code must be exactly 3 characters long'}), 400
        return func(*args, **kwargs)
    return wrapper

def validate_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        destination = request.args.get('destination')
        airlines = request.args.getlist('airlines')
        if not destination and not airlines:
            return jsonify({'error': 'Either destination or airlines should be provided to fetch the data'}), 400
        return func(*args, **kwargs)
    return wrapper
