from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_assignment():
    response = client.post("/assignments/", json={"title": "New Assignment", "description": "Assignment description", "start_date": "2024-09-01", "due_date": "2024-09-15", "class_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Assignment created"

def test_get_assignments():
    response = client.get("/assignments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
