from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db, auth_required

router = APIRouter()


@router.post('', response_model=schemas.salesman.Salesman, status_code=201)
@auth_required
def create_salesman(salesman: schemas.salesman.SalesmanCreate, db: Session = Depends(get_db)):
    db_salesman = actions.salesman.get_salesman_by_dni(db, dni=salesman.dni)
    if db_salesman:
        raise HTTPException(status_code=400, detail='Vendedor ya registrado')
    return actions.salesman.create_salesman(db=db, salesman=salesman)


@router.get('', response_model=list[schemas.salesman.Salesman])
@auth_required
def read_salesmen(namelike: str | None = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return actions.salesman.get_salesmen(db, namelike=namelike, skip=skip, limit=limit)


@router.get('/{dni}', response_model=schemas.salesman.Salesman)
@auth_required
def read_salesman(dni: int, db: Session = Depends(get_db)):
    db_salesman = actions.salesman.get_salesman_by_dni(db, dni=dni)
    if db_salesman is None:
        raise HTTPException(status_code=404, detail='Vendedor no encontrado')
    return db_salesman
