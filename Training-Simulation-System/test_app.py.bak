
import unittest
from app import app

class TrainingSimulationTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Training and Simulation System", response.get_json()["message"])

    def test_analyze_scenario(self):
        response = self.app.post('/analyze_scenario', json={"scenario_description": "Simulate disaster response."})
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.get_json())

    def test_simulate_geospatial(self):
        geospatial_data = {"latitude": 40.7128, "longitude": -74.0060, "event_type": "Evacuation Drill"}
        response = self.app.post('/simulate_geospatial', json=geospatial_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    def test_secure_data(self):
        secure_data_request = {"data": "Training data"}
        response = self.app.post('/secure_data', json=secure_data_request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("encrypted_data", response.get_json())

if __name__ == '__main__':
    unittest.main()
