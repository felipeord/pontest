"""Config for async session for DE MYSQL"""

from typing import AsyncGenerator
import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from main import app

BASE_URL = "http://test"


@pytest.fixture
def anyio_backend():
    """asyncio backend"""
    return "asyncio"


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, None]:
    """async client for test"""
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url=BASE_URL) as _client:
            try:
                yield _client
            finally:
                await _client.aclose()
