import pytest
from httpx import Client


@pytest.fixture
def client() -> Client:
    with Client(base_url="http://127.0.0.1:8000") as client:
        yield client
