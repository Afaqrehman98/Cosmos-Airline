from flask import request, jsonify
from functools import wraps

def validate_destination(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        destination = request.args.get('destination')
        if destination and len(destination) != 3:
            return jsonify({'error': 'Destination must be a 3-character airport code'}), 400
        return func(*args, **kwargs)
    return wrapper
