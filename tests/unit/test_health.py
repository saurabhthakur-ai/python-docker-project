"""Unit tests for health service."""

from app.services.health_service import get_health_status


def test_get_health_status():
    """Health status should report healthy."""
    result = get_health_status()

    assert result["status"] == "healthy"
    assert "timestamp" in result
