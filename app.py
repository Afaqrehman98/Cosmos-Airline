from flask import Flask,render_template
from views.flight_view import flight_bp
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
# Register blueprints
app.register_blueprint(flight_bp)

if __name__ == '__main__':
    app.run(debug=True)