from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "new_user", "password": "password123", "role": "teacher"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "admin"
