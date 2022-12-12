from datetime import timedelta

import sqlalchemy.exc
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db

ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()


@app.post('/token', response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = actions.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401,
                            detail='Incorrect username or password',
                            headers={'WWW-Authenticate': 'Bearer'})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = actions.create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.post('/register', response_model=schemas.User, status_code=201)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = actions.create_user(db=db, user=user)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=400, detail='Usuario ya registrado')
    return db_user


@app.get('/auth', response_model=schemas.User)
async def read_users_me(user: schemas.User = Depends(actions.get_current_user)):
    return user
