from fastapi.testclient import TestClient

from app import main

client = TestClient(main)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
