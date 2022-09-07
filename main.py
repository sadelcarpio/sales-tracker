from fastapi import FastAPI

from database import engine, Base
from routes import salesman, product, store

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(salesman.router, prefix='/salesman')
app.include_router(product.router, prefix='/product')
app.include_router(store.router, prefix='/store')
