import os

from fastapi import Request
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from dependencies import get_db, verify_token
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


def override_verify_token(req: Request):
    pass


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[verify_token] = override_verify_token

client = TestClient(app)


class TestSalesmen:

    def test_get_salesmen(self):
        response = client.get('/salesmen')
        assert response.status_code == 200


class TestStores:
    def test_get_stores(self):
        response = client.get('/stores')
        assert response.status_code == 200


class TestProducts:
    def test_get_products(self):
        response = client.get('/products')
        assert response.status_code == 200


class TestSales:

    def test_get_sales(self):
        response = client.get('/sales')
        assert response.status_code == 200
