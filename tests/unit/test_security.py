"""Unit tests for security utilities."""

from app.core.security import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password,
)


def test_password_hashing():
    """Password hashing and verification should work correctly."""
    password = "secret-password"
    hashed = get_password_hash(password)

    assert verify_password(password, hashed) is True
    assert verify_password("wrong-password", hashed) is False


def test_access_token_lifecycle():
    """Created tokens should be decodable and contain the subject."""
    data = {"sub": "testuser"}
    token = create_access_token(data)
    payload = decode_access_token(token)

    assert payload is not None
    assert payload["sub"] == "testuser"


def test_decode_invalid_token():
    """Decoding an invalid token should return None."""
    assert decode_access_token("not-a-valid-token") is None
