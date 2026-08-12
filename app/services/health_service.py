"""Health service."""

from datetime import datetime, timezone


def get_health_status() -> dict[str, str]:
    """Return a health status payload."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
