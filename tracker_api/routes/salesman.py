from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db, verify_token
import datetime

router = APIRouter(tags=["Salesman Endpoints"])


@router.get('', response_model=list[schemas.salesman.Salesman],
            dependencies=[Depends(verify_token)], status_code=200)
def read_salesmen(request: Request, namelike: str | None = None, skip: int = 0, limit: int = 10,
                  db: Session = Depends(get_db)):
    return actions.salesman.get_salesmen(db, namelike=namelike, skip=skip, limit=limit)


@router.get('/{dni}', response_model=schemas.salesman.Salesman,
            dependencies=[Depends(verify_token)], status_code=200)
def read_salesman_by_dni(request: Request, dni: str, db: Session = Depends(get_db)):
    db_salesman = actions.salesman.get_salesman_by_dni(db, dni=dni)
    if db_salesman is None:
        raise HTTPException(status_code=404, detail='Vendedor no encontrado')
    return db_salesman
