"""API routes."""

from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.services.health_service import get_health_status

router = APIRouter()

router.include_router(auth_router)


@router.get("/health", tags=["Health"])
async def api_health_check() -> dict[str, str]:
    """Return API health status."""
    return get_health_status()
