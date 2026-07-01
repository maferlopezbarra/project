from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

def test_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_file():
    with open("data/input/input.db", "rb") as file:
        response = client.post(
            "/displacements",
            files={
                "file": ("data/input/input.db", file, "application/octet-stream")
            },
            data={
                "elevation": 10300,
                "factor": 250
            }
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert "attachment" in response.headers["content-disposition"]