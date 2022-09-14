from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db, auth_required

router = APIRouter()


@router.post('', response_model=schemas.store.Store, status_code=201)
@auth_required
def create_store(store: schemas.store.StoreCreate, db: Session = Depends(get_db)):
    db_store = actions.store.get_store_by_ruc(db, ruc_or_dni=store.ruc_or_dni)
    if db_store:
        raise HTTPException(status_code=400, detail='Tienda ya registrada')
    return actions.store.create_store(db=db, store=store)


@router.get('', response_model=list[schemas.store.Store])
@auth_required
def read_stores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_stores = actions.store.get_stores(db, skip=skip, limit=limit)
    return db_stores


@router.get('/{ruc_or_dni}', response_model=schemas.store.Store)
@auth_required
def read_store(ruc_or_dni: int, db: Session = Depends(get_db)):
    db_store = actions.store.get_store_by_ruc(db, ruc_or_dni=ruc_or_dni)
    if db_store is None:
        raise HTTPException(status_code=404, detail='Tienda no encontrada')
    return db_store
