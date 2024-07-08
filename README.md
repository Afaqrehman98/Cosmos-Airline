# Cosmos Flight Service

## Introduction

Cosmos Flight Service is a Flask-based API service designed to fetch and display flight information based on destination airports and airline codes. It integrates with external APIs to provide real-time data on flight schedules and delays.

## Installation Guide

Follow these steps to set up and run the Cosmos Flight Service locally:

1. **Clone the Repository:**
   git clone https://github.com/Afaqrehman98/Cosmos-Airline
   cd cosmos-flight-service

2. **Create and Activate Virtual Environment:**

python -m venv venv

# On Windows

venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the Application:**

python app.py

## Port Information

The application runs on port 5000 by default. Access it at http://localhost:5000.

## Libraries Used

Flask: Micro web framework for Python
Flask-CORS: Flask extension for handling Cross-Origin Resource Sharing
requests: HTTP library for making requests to external APIs
Screenshots of Testing via Postman
Successful Request

## Invalid Destination

## Missing Parameters

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
