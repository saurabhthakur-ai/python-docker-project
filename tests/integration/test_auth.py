"""Integration tests for authentication endpoints."""


def test_register_user(client):
    """User registration should return the created user."""
    payload = {
        "username": "johndoe",
        "email": "john@example.com",
        "password": "secret123",
        "name": "John Doe",
        "age": 30,
        "address": "123 Main St",
        "phone_no": "+1234567890",
    }
    response = client.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "johndoe"
    assert data["email"] == "john@example.com"
    assert data["name"] == "John Doe"
    assert "id" in data
    assert "password" not in data


def test_register_duplicate_user(client):
    """Registering the same username twice should fail."""
    payload = {
        "username": "johndoe",
        "email": "john@example.com",
        "password": "secret123",
        "name": "John Doe",
    }
    client.post("/api/v1/auth/register", json=payload)
    response = client.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 400


def test_login_and_access_me(client):
    """Login should return a token that can access the /me endpoint."""
    register_payload = {
        "username": "janedoe",
        "email": "jane@example.com",
        "password": "secret123",
        "name": "Jane Doe",
    }
    client.post("/api/v1/auth/register", json=register_payload)

    login_response = client.post(
        "/api/v1/auth/login",
        data={"username": "janedoe", "password": "secret123"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["username"] == "janedoe"


def test_login_invalid_credentials(client):
    """Login with invalid credentials should return 401."""
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "nobody", "password": "wrong"},
    )

    assert response.status_code == 401


def test_logout(client):
    """Logout endpoint should return a success message."""
    response = client.post("/api/v1/auth/logout")

    assert response.status_code == 200
    assert response.json()["message"] == "Successfully logged out"
