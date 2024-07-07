from flask import Flask
from controllers.flight_controller import flight_bp
from middlewares.validation_middleware import validate_request

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(flight_bp)

# Register Middleware
app.before_request(validate_request)

if __name__ == '__main__':
    app.run(debug=True)
