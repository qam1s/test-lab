from httpx import Client


def test_health(client: Client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
