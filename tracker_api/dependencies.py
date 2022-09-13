# Dependency
import os
from functools import wraps

from fastapi import HTTPException

import requests
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def auth_call():
    try:
        # TODO: Pasar el token al header del request.
        token = requests.post(url=os.getenv('TOKEN_URL'),
                              data={
                                  'username': 'johndoe',  # Mock DB
                                  'password': 'secret'
                              })
        token.raise_for_status()
        response = requests.get(url=os.getenv('ACCESS_URL'),
                                headers={'Authorization': 'Bearer ' + token.json()['access_token']})
        response.raise_for_status()
    except requests.HTTPError as error:
        # TODO: mejorar descripciones de error
        raise HTTPException(status_code=401, detail=str(error))


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_call()
        return func(*args, **kwargs)
    return wrapper
