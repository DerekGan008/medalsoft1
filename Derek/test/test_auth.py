from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/auth/login", data={"username": "DEREK", "password": "Derekgan"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_current_user():
    token = "your_test_token_here"
    response = client.get("/auth/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "admin"
