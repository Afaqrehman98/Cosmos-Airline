import unittest
from app import app

class FlightInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_flight_info_success(self):
        response = self.app.get('/get_flight_info?destination=MUC&airlines=LH')
        self.assertEqual(response.status_code, 200)
        self.assertIn('flight_number', response.json[0])

    def test_get_flight_info_invalid_destination(self):
        response = self.app.get('/get_flight_info?destination=MUCA')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Destination airport code must be exactly 3 characters long')

if __name__ == '__main__':
    unittest.main()
