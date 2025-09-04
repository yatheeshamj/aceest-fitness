import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from app import app, workouts

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        workouts.clear()
        yield client

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}

def test_add_and_get_workouts(client):
    r = client.post("/workouts", json={"workout": "Running", "duration": 30})
    assert r.status_code == 201

    r2 = client.get("/workouts")
    assert r2.status_code == 200
    data = r2.get_json()
    assert isinstance(data, list)
    assert {"workout": "Running", "duration": 30} in data

def test_validation_errors(client):
    assert client.post("/workouts", json={"workout": "", "duration": 10}).status_code == 400
    assert client.post("/workouts", json={"workout": "Swim"}).status_code == 400
    assert client.post("/workouts", json={"workout": "Swim", "duration": "abc"}).status_code == 400
    assert client.post("/workouts", json={"workout": "Swim", "duration": 0}).status_code == 400
