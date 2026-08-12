# ── Test the health-check and index endpoints ──────────────────────────────

import pytest

from app.main import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_json_with_status_ok(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "ok"


def test_health_contains_uptime(client):
    response = client.get("/health")
    data = response.get_json()
    assert "uptime_seconds" in data


def test_health_contains_environment(client):
    response = client.get("/health")
    data = response.get_json()
    assert "environment" in data


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_returns_welcome_message(client):
    response = client.get("/")
    data = response.get_json()
    assert "message" in data
