from geojson import Point, Feature, FeatureCollection
import random
import time
import logging
from typing import Dict

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class GeospatialMonitor:
    def __init__(self, region_bounds: Dict[str, float]):
        """
        Initialize the geospatial monitor with region boundaries.
        :param region_bounds: A dictionary with 'lat_min', 'lat_max', 'lon_min', 'lon_max'.
        """
        self.region_bounds = region_bounds

    def simulate_event(self) -> Feature:
        """
        Simulate a geospatial event within the region bounds.
        :return: A GeoJSON Feature representing the event.
        """
        lat = random.uniform(self.region_bounds['lat_min'], self.region_bounds['lat_max'])
        lon = random.uniform(self.region_bounds['lon_min'], self.region_bounds['lon_max'])
        event_type = random.choice(['Intrusion', 'Sensor Trigger', 'Anomaly', 'Data Spike'])

        point = Point((lon, lat))
        feature = Feature(geometry=point, properties={
            "event": event_type,
            "timestamp": time.time()
        })

        logging.info(f"Simulated event: {feature}")
        return feature

    def simulate_collection(self, count: int = 5) -> FeatureCollection:
        """
        Simulate a collection of events.
        :param count: Number of events to simulate.
        :return: A GeoJSON FeatureCollection.
        """
        features = [self.simulate_event() for _ in range(count)]
        return FeatureCollection(features)
