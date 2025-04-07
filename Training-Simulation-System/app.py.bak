
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import geojson
from transformers import pipeline
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize AI models (e.g., NLP for training scenario analysis)
scenario_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return jsonify({
        "message": "Training and Simulation System repository is fully functional.",
        "features": [
            "AI-Powered Training Scenarios",
            "Real-Time Collaboration",
            "Geospatial Simulations",
            "Secure Data Handling"
        ]
    })

@app.route('/analyze_scenario', methods=['POST'])
def analyze_scenario():
    data = request.json.get("scenario_description", "")
    if not data:
        return jsonify({"error": "No scenario description provided"}), 400
    analysis = scenario_analyzer(data)
    return jsonify({"analysis": analysis})

@app.route('/simulate_geospatial', methods=['POST'])
def simulate_geospatial():
    data = request.json
    if not data or "latitude" not in data or "longitude" not in data:
        return jsonify({"error": "Invalid geospatial data"}), 400

    simulation_event = geojson.Feature(
        geometry=geojson.Point((data["longitude"], data["latitude"])),
        properties={"event_type": data.get("event_type", "Training Event")}
    )
    socketio.emit("simulation_event", {"event": geojson.dumps(simulation_event)})
    return jsonify({"message": "Geospatial simulation triggered successfully", "event": simulation_event})

@app.route('/secure_data', methods=['POST'])
def secure_data():
    data = request.json.get("data", "").encode()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    return jsonify({"encrypted_data": encrypted_data.hex(), "iv": iv.hex()})

@socketio.on('simulation_update')
def handle_simulation_update(data):
    emit("receive_update", data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5004)
