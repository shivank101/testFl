import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/ping')
    assert resp.status_code == 200