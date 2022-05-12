from fastapi.testclient import TestClient

from app.main import *
from app import celery_worker

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
