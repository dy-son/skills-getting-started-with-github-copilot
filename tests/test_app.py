from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

client = TestClient(app)
original_activities = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(original_activities))
    yield
    activities.clear()
    activities.update(deepcopy(original_activities))


def test_get_activities_returns_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert data["Chess Club"]["description"] == "Learn strategies and compete in chess tournaments"
    assert data["Chess Club"]["participants"] == ["michael@mergington.edu", "daniel@mergington.edu"]


def test_signup_for_activity_returns_success():
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "test@mergington.edu"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@mergington.edu for Chess Club"
    assert "test@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_duplicate_participant_returns_400():
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "michael@mergington.edu"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
    assert activities["Chess Club"]["participants"].count("michael@mergington.edu") == 1


def test_remove_participant_returns_success():
    response = client.delete(
        "/activities/Chess Club/participants", params={"email": "michael@mergington.edu"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_remove_nonexistent_participant_returns_404():
    response = client.delete(
        "/activities/Chess Club/participants", params={"email": "missing@mergington.edu"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
