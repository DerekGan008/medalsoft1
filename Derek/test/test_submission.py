from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_submission():
    response = client.post("/submissions/", json={"student_id": 3, "assignment_id": 1, "content": "path/to/submission.pdf"})
    assert response.status_code == 200
    assert response.json()["message"] == "Submission created"

def test_get_submissions():
    response = client.get("/submissions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
