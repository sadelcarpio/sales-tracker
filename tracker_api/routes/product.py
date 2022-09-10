from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import actions
import schemas
from dependencies import get_db

router = APIRouter()


@router.post('', response_model=schemas.product.Product, status_code=201)
def create_product(product: schemas.product.ProductCreate, db: Session = Depends(get_db)):
    return actions.product.create_product(db=db, product=product)


@router.get('', response_model=list[schemas.product.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return actions.product.get_products(db, skip=skip, limit=limit)


@router.get('/{identifier}', response_model=schemas.product.Product)
def read_product(identifier: int, db: Session = Depends(get_db)):
    db_product = actions.product.get_product(db, identifier=identifier)
    if db_product is None:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
    return db_product
