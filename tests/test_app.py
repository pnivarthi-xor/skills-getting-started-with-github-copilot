import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_for_activity():
    response = client.post("/activities/Tennis Club/signup?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@example.com for Tennis Club"


def test_unregister_from_activity():
    response = client.post("/activities/Tennis Club/unregister?email=test@example.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered test@example.com from Tennis Club"