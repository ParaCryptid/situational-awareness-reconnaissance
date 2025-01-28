
import unittest
from app import app

class SituationalAwarenessTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Situational Awareness and Reconnaissance", response.get_json()["message"])

    def test_analyze_data(self):
        response = self.app.post('/analyze_data', json={"recon_data": "Unusual activity detected near the border."})
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.get_json())

    def test_generate_map(self):
        map_data = {"latitude": 34.05, "longitude": -118.25, "event": "Reconnaissance Event"}
        response = self.app.post('/generate_map', json=map_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    def test_secure_recon_data(self):
        secure_data_request = {"data": "Mission-critical information"}
        response = self.app.post('/secure_recon_data', json=secure_data_request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("encrypted_data", response.get_json())

if __name__ == '__main__':
    unittest.main()
