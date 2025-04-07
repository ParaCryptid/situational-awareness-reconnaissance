
import random
import time
import json
import os

SENSOR_LOG = "/opt/training-system/logs/sensor_feed.json"

def generate_sensor_data():
    return {
        "timestamp": time.time(),
        "radiation": round(random.uniform(0.1, 5.0), 2),  # microsieverts/hour
        "bio_agent": random.choice(["None", "Anthrax", "Botulinum", "Ricin"]),
        "chem_level": round(random.uniform(0.0, 100.0), 1),  # ppm
        "gps": {
            "lat": round(random.uniform(-90, 90), 6),
            "lon": round(random.uniform(-180, 180), 6)
        }
    }

def write_sensor_feed():
    os.makedirs(os.path.dirname(SENSOR_LOG), exist_ok=True)
    print("[SENSOR] Generating synthetic sensor data...")
    while True:
        data = generate_sensor_data()
        with open(SENSOR_LOG, "a") as f:
            f.write(json.dumps(data) + "\n")
        time.sleep(5)
