
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import geojson
import folium
from transformers import pipeline
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize AI models (e.g., NLP for reconnaissance analysis)
reconnaissance_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return jsonify({
        "message": "Situational Awareness and Reconnaissance repository is fully functional.",
        "features": [
            "AI-Powered Situational Analysis",
            "Geospatial Intelligence",
            "Real-Time Monitoring",
            "Secure Data Handling"
        ]
    })

@app.route('/analyze_data', methods=['POST'])
def analyze_data():
    data = request.json.get("recon_data", "")
    if not data:
        return jsonify({"error": "No reconnaissance data provided"}), 400
    analysis = reconnaissance_analyzer(data)
    return jsonify({"analysis": analysis})

@app.route('/generate_map', methods=['POST'])
def generate_map():
    data = request.json
    if not data or "latitude" not in data or "longitude" not in data:
        return jsonify({"error": "Invalid geospatial data"}), 400

    map_ = folium.Map(location=[data["latitude"], data["longitude"]], zoom_start=13)
    folium.Marker([data["latitude"], data["longitude"]], popup=data.get("event", "Reconnaissance Event")).add_to(map_)
    map_file = "map.html"
    map_.save(map_file)
    return jsonify({"message": "Geospatial map generated successfully", "map_file": map_file})

@app.route('/secure_recon_data', methods=['POST'])
def secure_recon_data():
    data = request.json.get("data", "").encode()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    return jsonify({"encrypted_data": encrypted_data.hex(), "iv": iv.hex()})

@socketio.on('broadcast_update')
def broadcast_update(data):
    emit("receive_update", data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5005)
