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
  ```

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

- ### Successful Request:

  - **With Airline & Destination as a Parameter:**

  ![API-Success-Destination-Airline](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/db20a4c4-9dc4-4eec-a762-bf5de24430b9)

  - **With Destination as a Parameter:**

  ![API-Success-Destination](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/ec931b65-a7bc-4a0d-acf1-df2849c386eb)

  - **Multiple Airlines as Destination as a Parameter:**

  ![API-Success-Multiple-Airline](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/fc2b2ed7-a2a0-47a2-b986-1c8a7bed9e4b)

- ### Empty Parameters

  ![API-Error-No-Parameters](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/7b64b43d-56d3-4330-b0f1-23384d6fee66)

- ### Destination with less than 3 characters:
  ![API-Error-Destination-Less-Character](https://github.com/Afaqrehman98/Cosmos-Airline/assets/62624461/4a13c255-da10-4acf-9b60-84f9b89533b0)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
