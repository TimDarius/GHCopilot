def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert "Chess Club" in payload

    chess_club = payload["Chess Club"]
    assert chess_club == {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    }


def test_get_activities_returns_expected_activity_shape(client):
    response = client.get("/activities")

    payload = response.json()
    first_activity = next(iter(payload.values()))

    assert set(first_activity) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(first_activity["participants"], list)
