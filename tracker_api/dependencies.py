# Dependency
import os
from functools import wraps

import requests
from fastapi import HTTPException

from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def auth_call(token: str):
    if token is not None:
        response = requests.get(url=os.getenv('AUTH_URL'),
                                headers={'Authorization': token})
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()['detail'])
    else:
        raise HTTPException(status_code=400, detail='No authorization header')


def auth_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        auth_call(request.headers.get('Authorization'))
        return func(request, *args, **kwargs)

    return wrapper
