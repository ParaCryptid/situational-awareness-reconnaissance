import requests

class IoTDataCollector:
    def __init__(self, endpoints):
        """
        Initialize the collector with a list of IoT endpoints.
        :param endpoints: List of public IoT device endpoints (URLs).
        """
        self.endpoints = endpoints

    def collect_data(self):
        """
        Collect data from all IoT endpoints.
        :return: A dictionary of data collected from each endpoint.
        """
        collected_data = {}
        for endpoint in self.endpoints:
            try:
                response = requests.get(endpoint, timeout=5)
                if response.status_code == 200:
                    collected_data[endpoint] = response.json()  # Assuming JSON responses
                else:
                    collected_data[endpoint] = f"Error: {response.status_code}"
            except Exception as e:
                collected_data[endpoint] = f"Error: {str(e)}"
        return collected_data

# Example usage
# endpoints = ["http://iot-device1.local/data", "http://weather-station.local/api"]
# collector = IoTDataCollector(endpoints)
# data = collector.collect_data()
# print(data)
