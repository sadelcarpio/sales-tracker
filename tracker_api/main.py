import os

import uvicorn
from fastapi import FastAPI

from database import engine, Base
from routes import salesman, sale, store, product

app = FastAPI()

app.include_router(salesman.router, prefix='/salesmen')
app.include_router(sale.router, prefix='/sales')
app.include_router(store.router, prefix='/stores')
app.include_router(product.router, prefix='/products')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv('PORT', default=8000)))
