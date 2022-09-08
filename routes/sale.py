from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db

router = APIRouter()


@router.post('/{id_salesman}/{id_store}/{id_product}', response_model=schemas.sale.Sale, status_code=201)
def create_sale(id_salesman: int, id_store: int, id_product: int,
                sale: schemas.sale.SaleCreate, db: Session = Depends(get_db)):
    return actions.sale.create_sale(db=db, sale=sale, id_salesman=id_salesman,
                                    id_store=id_store, id_product=id_product)


@router.get('', response_model=list[schemas.sale.Sale])
def read_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sales = actions.sale.get_sales(db, skip=skip, limit=limit)
    return sales
