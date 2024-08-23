from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_class():
    response = client.post("/classes/", json={"name": "New Class", "description": "Class description"})
    assert response.status_code == 200
    assert response.json()["message"] == "Class created"

def test_get_classes():
    response = client.get("/classes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
