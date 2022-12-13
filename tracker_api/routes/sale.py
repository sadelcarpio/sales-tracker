import datetime

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db, verify_token

router = APIRouter(tags=["Sales Endpoints"])


@router.post('', response_model=schemas.sale.Sale,
             dependencies=[Depends(verify_token)], status_code=201)
def create_sale(request: Request, id_salesman: int, id_store: int, id_product: int,
                sale: schemas.sale.SaleCreate, db: Session = Depends(get_db)):
    return actions.sale.create_sale(db=db, sale=sale, id_salesman=id_salesman,
                                    id_store=id_store, id_product=id_product)


@router.get('', response_model=list[schemas.sale.Sale],
            dependencies=[Depends(verify_token)], status_code=200)
def read_sales(request: Request, salesman_id: int | None = None, store_id: int | None = None,
               product_id: int | None = None, date: datetime.date | None = None, skip: int = 0, limit: int = 10,
               db: Session = Depends(get_db)):
    db_sales = actions.sale.get_sales(db=db, salesman_id=salesman_id, store_id=store_id, product_id=product_id,
                                      date=date, skip=skip, limit=limit)
    return db_sales
