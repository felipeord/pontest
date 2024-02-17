"""Test main route """
import pytest
from httpx import AsyncClient
from app.config.settings import settings


@pytest.mark.anyio
async def test_root(client: AsyncClient) -> None:
    """Test root"""
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "service": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
    }
