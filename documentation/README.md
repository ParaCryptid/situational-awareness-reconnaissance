
# Situational Awareness & Reconnaissance

## Overview
The Situational Awareness & Reconnaissance repository has been enhanced to include advanced AI analysis, geospatial intelligence, real-time monitoring, and secure data handling.

### New Features
1. **AI-Powered Situational Analysis**
    - Endpoint: `/analyze_data`
    - Method: `POST`
    - Description: Analyzes reconnaissance data for sentiment and insights.
    - Example Request:
      ```json
      {
          "recon_data": "Unusual activity detected near the northern border."
      }
      ```
    - Example Response:
      ```json
      {
          "analysis": [{"label": "NEGATIVE", "score": 0.98}]
      }
      ```

2. **Geospatial Intelligence**
    - Endpoint: `/generate_map`
    - Method: `POST`
    - Description: Generates an interactive map with event markers based on geospatial data.
    - Example Request:
      ```json
      {
          "latitude": 34.05,
          "longitude": -118.25,
          "event": "Reconnaissance Event"
      }
      ```
    - Example Response:
      ```json
      {
          "message": "Geospatial map generated successfully",
          "map_file": "map.html"
      }
      ```

3. **Secure Data Handling**
    - Endpoint: `/secure_recon_data`
    - Method: `POST`
    - Description: Encrypts reconnaissance data for secure storage or transmission.
    - Example Request:
      ```json
      {
          "data": "Reconnaissance mission details"
      }
      ```
    - Example Response:
      ```json
      {
          "encrypted_data": "abc123...",
          "iv": "456def..."
      }
      ```

4. **Real-Time Monitoring**
    - Enables real-time updates for situational awareness using Flask-SocketIO.
    - Events:
      - `broadcast_update`: Send an update to all connected clients.
      - `receive_update`: Receive broadcasted updates.

### Getting Started
1. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python app.py
    ```
