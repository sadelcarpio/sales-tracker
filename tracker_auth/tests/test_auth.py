import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.fixture()
def token():
    response = client.post('/token', data={'username': 'sdelcarpio@gmail.com', 'password': 'sergio'})
    return response.json().get('access_token')


def test_token():
    response = client.post('/token', data={'username': 'sdelcarpio@gmail.com', 'password': 'sergio'})
    assert response.status_code == 200
    assert response.json().get('access_token') is not None


def test_auth(token):
    auth_response = client.get('/auth', headers={'Authorization': 'Bearer ' + token})
    assert auth_response.status_code == 200
    assert auth_response.json() == {
        "id": 1,
        "name": "Sergio Del Carpio",
        "dni": 75482000,
        "username": "sdelcarpio@gmail.com"
    }


def test_register(token):
    register_response = client.post('/register', json={
        "name": "Rosanella Alarcon",
        "dni": "09458777",
        "username": "ralarcon@gmail.com",
        "password": "chane"
    })
    assert register_response.status_code == 400
    assert register_response.json().get('detail') == 'Usuario ya registrado'
