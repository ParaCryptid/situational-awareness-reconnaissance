
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Situational Awareness and Reconnaissance System is fully functional.' in response.data

# Test adding a log
def test_add_log(client):
    data = {"content": "Suspicious activity detected near checkpoint."}
    response = client.post('/add_log', json=data)
    assert response.status_code == 200
    assert "Log added successfully." in response.get_json()["message"]

# Test retrieving logs
def test_get_logs(client):
    response = client.get('/get_logs')
    assert response.status_code == 200
    logs = response.get_json()
    assert isinstance(logs, list)
    assert len(logs) > 0

# Test searching logs
def test_search_logs(client):
    data = {"content": "Checkpoint clear."}
    client.post('/add_log', json=data)  # Add a log for testing

    search_response = client.get('/search_logs?keyword=checkpoint')
    assert search_response.status_code == 200
    filtered_logs = search_response.get_json()
    assert len(filtered_logs) > 0

# Test deleting a log
def test_delete_log(client):
    # Add a log to delete
    data = {"content": "Test log for deletion."}
    add_response = client.post('/add_log', json=data)
    log_id = add_response.get_json()["log"]["id"]

    # Delete the log
    delete_response = client.delete('/delete_log', json={"id": log_id})
    assert delete_response.status_code == 200
    assert "Log deleted successfully." in delete_response.get_json()["message"]
