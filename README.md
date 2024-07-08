# Cosmos Flight Service

## Introduction

Cosmos Flight Service is a Flask-based API service designed to fetch and display flight information based on destination airports and airline codes. It integrates with external APIs to provide real-time data on flight schedules and delays.

## Installation Guide

Follow these steps to set up and run the Cosmos Flight Service locally:

### Step 1: Clone the Repository

- Open your terminal or command prompt
- Run the following commands: 
   ```
   git clone https://github.com/Afaqrehman98/Cosmos-Airline
   cd cosmos-flight-service

### Step 2: Create and Activate Virtual Environment:
   ```
   python -m venv venv
   ```
- On Windows
   ```
   venv\Scripts\activate
   ```
- On macOS/Linux
    ```
    source venv/bin/activate
    ```

### Step 3: Install Dependencies:
   ```
   pip install -r requirements.txt
   ```


### Step 4: Run the Application:
   ```
   python app.py
   ```

## Port Information

The application runs on port 5000 by default. 
Access it at [http://127.0.0.1:5000/get_flight_info?].


## Libraries Used

- **Flask:** Micro web framework for Python
- **Flask-CORS:** Flask extension for handling Cross-Origin Resource Sharing
- **requests:** HTTP library for making requests to external APIs
- **unittest2:** Library for writing unit tests


## Screenshots of Testing via Postman

### Successful Request:
![WhatsApp Image 2024-07-07 at 23 00 40](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/92fd5828-3a98-4bd9-ba49-a2c904152128)


### Invalid Destination

### Missing Parameters


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
    
