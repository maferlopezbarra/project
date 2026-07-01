from fastapi.testclient import TestClient
from io import BytesIO

from src.api import app

client = TestClient(app)


def test_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


'''def test_input_output():
    with open("data/input/input.db", "rb") as file:
        response = client.post(
            "/displacements",
            files={"file": ("data/input/input.db", file, "application/octet-stream")},
            data={"elevation": 10300, "factor": 250},
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert "attachment" in response.headers["content-disposition"]'''

def test_input_output():
    with open("data/input/input.db", "rb") as file:
        response = client.post(
            "/displacements",
            files={"file": ("data/input/input.db", file, "application/octet-stream")},
            data={"elevation": 10300, "factor": 250},
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert "attachment" in response.headers["content-disposition"]

'''def test_file_type():
    response = client.post(
        "/displacements",
        files={"file": ("input.txt", BytesIO(b"txt"), "text/plain")},
        data={"elevation": 10300, "factor": 250},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Only .db files are accepted"}'''

def test_file_type():
    response = client.post(
        "/displacements",
        files={"file": ("input.txt", BytesIO(b"txt"), "text/plain")},
        data={"elevation": 10300, "factor": 250},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Only .db files are accepted"}