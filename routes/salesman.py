from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db

router = APIRouter()


@router.post('', response_model=schemas.salesman.Salesman, status_code=201)
def create_salesman(salesman: schemas.salesman.SalesmanCreate, db: Session = Depends(get_db)):
    salesmen = actions.salesman.get_salesman(db, dni=salesman.dni)
    if salesmen:
        raise HTTPException(status_code=400, detail='Vendedor ya registrado')
    return actions.salesman.create_salesman(db=db, salesman=salesman)


@router.get('', response_model=list[schemas.salesman.Salesman])
def read_salesmen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    salesmen = actions.salesman.get_salesmen(db, skip=skip, limit=limit)
    return salesmen


@router.get('/{dni}', response_model=schemas.salesman.Salesman)
def read_salesman(dni: int, db: Session = Depends(get_db)):
    db_salesman = actions.salesman.get_salesman(db, dni=dni)
    if db_salesman is None:
        raise HTTPException(status_code=404, detail='Vendedor no encontrado')
    return db_salesman
