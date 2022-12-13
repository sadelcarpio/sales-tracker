# Dependency
import os
from functools import wraps

import requests
from fastapi import HTTPException, Request

from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_token(req: Request):
    token = req.headers.get('Authorization')
    if token is not None:
        response = requests.get(url=os.getenv('AUTH_URL'),
                                headers={'Authorization': token})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()['detail'])
    else:
        raise HTTPException(status_code=400, detail='No authorization header')
