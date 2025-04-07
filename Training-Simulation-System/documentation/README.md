
# Training Simulation System

## Overview
The Training Simulation System has been enhanced to provide advanced AI-powered scenarios, real-time collaboration, geospatial simulations, and secure data handling.

### New Features
1. **AI-Powered Training Scenarios**
    - Endpoint: `/analyze_scenario`
    - Method: `POST`
    - Description: Analyzes training scenarios for sentiment and insights.
    - Example Request:
      ```json
      {
          "scenario_description": "Simulate an emergency response to a fire in a densely populated area."
      }
      ```
    - Example Response:
      ```json
      {
          "analysis": [{"label": "POSITIVE", "score": 0.89}]
      }
      ```

2. **Real-Time Collaboration**
    - Enables real-time updates and interactions for collaborative simulations using Flask-SocketIO.

3. **Geospatial Simulations**
    - Endpoint: `/simulate_geospatial`
    - Method: `POST`
    - Description: Triggers geospatial events for training scenarios.
    - Example Request:
      ```json
      {
          "latitude": 40.7128,
          "longitude": -74.0060,
          "event_type": "Evacuation Drill"
      }
      ```
    - Example Response:
      ```json
      {
          "message": "Geospatial simulation triggered successfully",
          "event": {...}
      }
      ```

4. **Secure Data Handling**
    - Endpoint: `/secure_data`
    - Method: `POST`
    - Description: Encrypts sensitive training data for secure storage or transmission.
    - Example Request:
      ```json
      {
          "data": "Training simulation records"
      }
      ```
    - Example Response:
      ```json
      {
          "encrypted_data": "abc123...",
          "iv": "456def..."
      }
      ```

### Getting Started
1. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python app.py
    ```
