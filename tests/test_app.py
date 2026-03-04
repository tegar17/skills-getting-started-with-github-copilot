import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    # Adjust the assertion below to match your actual root endpoint response
    # assert response.json() == {"message": "Hello, World!"}
