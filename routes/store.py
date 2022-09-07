from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db

router = APIRouter()


@router.post('', response_model=schemas.store.Store, status_code=201)
def create_product(store: schemas.store.StoreCreate, db: Session = Depends(get_db)):
    db_store = actions.store.get_store(db, ruc_or_dni=store.ruc_or_dni)
    if db_store:
        raise HTTPException(status_code=400, detail='Tienda ya registrada')
    return actions.store.create_store(db=db, store=store)


@router.get('', response_model=list[schemas.store.Store])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stores = actions.store.get_stores(db, skip=skip, limit=limit)
    return stores
