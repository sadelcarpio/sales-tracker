import pytest
import requests
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.fixture()
def token():
    response = requests.post('http://127.0.0.1:8001/token',
                             data={'username': 'sdelcarpio@gmail.com', 'password': 'sergio'})
    return response.json().get('access_token')


def test_salesmen(token):
    response = client.get('/salesmen', headers={'Authorization': 'Bearer ' + token})
    assert response.status_code == 200
