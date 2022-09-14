import datetime

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db, auth_required

router = APIRouter()


@router.post('', response_model=schemas.sale.Sale, status_code=201)
@auth_required
def create_sale(request: Request, id_salesman: int, id_store: int, id_product: int,
                sale: schemas.sale.SaleCreate, db: Session = Depends(get_db)):
    return actions.sale.create_sale(db=db, sale=sale, id_salesman=id_salesman,
                                    id_store=id_store, id_product=id_product)


@router.get('', response_model=list[schemas.sale.Sale])
@auth_required
def read_sales(request: Request, id_salesman: int | None = None, id_store: int | None = None,
               id_product: int | None = None, date: datetime.date | None = None, skip: int = 0, limit: int = 10,
               db: Session = Depends(get_db)):
    db_sales = actions.sale.get_sales(db=db, id_salesman=id_salesman, id_store=id_store, id_product=id_product,
                                      date=date, skip=skip, limit=limit)
    return db_sales
