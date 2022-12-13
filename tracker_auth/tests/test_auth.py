import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from actions import create_user, pwd_context
from dependencies import get_db
from models import User
from database import Base
from main import app

TEST_DB_URL = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@sales_tracker_postgres:5432/test_db'
engine = create_engine(TEST_DB_URL)

TestingSessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture
def token():
    response = client.post('/token', data={'username': 'sergio', 'password': 'sergio'})
    return response.json().get('access_token')


def setup_function():
    user = {'name': 'sergio', 'dni': 1234567, 'username': 'sergio'}
    db = TestingSessionLocal()
    hashed_password = pwd_context.hash('sergio')
    db_user = User(id=1, **user, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def test_token():
    response = client.post('/token', data={'username': 'sergio', 'password': 'sergio'})
    assert response.status_code == 200
    assert response.json().get('access_token') is not None


def test_auth(token):
    auth_response = client.get('/auth', headers={'Authorization': 'Bearer ' + token})
    assert auth_response.status_code == 200
    assert auth_response.json() == {
        "id": 1,
        "name": "sergio",
        "dni": 1234567,
        "username": "sergio"
    }


def test_already_registered():
    new_user = {
        "name": "sergio",
        "dni": 1234567,
        "username": "sergio",
        "password": "sergio"
    }
    register_response = client.post('/register', json=new_user)
    assert register_response.status_code == 400
    assert register_response.json().get('detail') == 'Usuario ya registrado'


def test_register():
    new_user = {
        "name": "Rosanella Alarcon",
        "dni": "09458777",
        "username": "ralarcon@gmail.com",
        "password": "chane"
    }
    register_response = client.post('/register', json=new_user)
    assert register_response.status_code == 201


def teardown_function():
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())
