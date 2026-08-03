from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["message"] == "AI Engineer Toolkit API running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_predict():
    response = client.post(
        "/predict",
        json={
            "age": 45,
            "salary": 80000
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "prediction" in body

    assert body["model"] == "LogisticRegression"

def test_api_title():
    response = client.get("/openapi.json")

    assert response.status_code == 200

    assert (
        response.json()["info"]["title"]
        == "AI Engineer Toolkit API"
    )