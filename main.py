from fastapi import FastAPI

from database import engine, Base
from routes import salesman

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(salesman.router, prefix='/salesman')
