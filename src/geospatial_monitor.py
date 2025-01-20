from geojson import Point, Feature, FeatureCollection
import random
import time

class GeospatialMonitor:
    def __init__(self, region_bounds):
        """
        Initialize the geospatial monitor with region boundaries.
        :param region_bounds: A dictionary with 'lat_min', 'lat_max', 'lon_min', 'lon_max'.
        """
        self.region_bounds = region_bounds

    def simulate_event(self):
        """
        Simulate a geospatial event within the region bounds.
        :return: A GeoJSON feature representing the event.
        """
        lat = random.uniform(self.region_bounds["lat_min"], self.region_bounds["lat_max"])
        lon = random.uniform(self.region_bounds["lon_min"], self.region_bounds["lon_max"])
        point = Point((lon, lat))
        event_type = random.choice(["Protest", "Traffic Incident", "Power Outage"])
        feature = Feature(geometry=point, properties={"event_type": event_type, "risk_level": random.randint(1, 5)})
        return feature

    def monitor_region(self, interval=5):
        """
        Continuously monitor the region and report events.
        :param interval: Time interval (in seconds) between event simulations.
        """
        while True:
            event = self.simulate_event()
            print(f"New Event: {event}")
            time.sleep(interval)

# Example usage
# bounds = {"lat_min": 34.0, "lat_max": 36.0, "lon_min": -118.0, "lon_max": -117.0}
# monitor = GeospatialMonitor(bounds)
# monitor.monitor_region(interval=10)
