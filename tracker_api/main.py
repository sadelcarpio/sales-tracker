from fastapi import FastAPI

from database import engine, Base
from dependencies import verify_token
from routes import salesman, sale, store, product

app = FastAPI()

app.include_router(salesman.router, prefix='/salesmen')
app.include_router(sale.router, prefix='/sales')
app.include_router(store.router, prefix='/stores')
app.include_router(product.router, prefix='/products')
app.dependency_overrides[verify_token] = lambda: None

Base.metadata.create_all(bind=engine)
