from fastapi import FastAPI

from database import engine, Base
from routes import salesman, sale, store, product

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(salesman.router, prefix='/salesmen')
app.include_router(sale.router, prefix='/sales')
app.include_router(store.router, prefix='/stores')
app.include_router(product.router, prefix='/products')
