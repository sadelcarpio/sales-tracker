import datetime

from sqlalchemy.orm import Session

import models
import schemas


def get_sales(db: Session, id_salesman: int | None = None, id_store: int | None = None, id_product: int | None = None,
              date: datetime.date | None = None, skip: int = 0, limit: int = 10):
    query = db.query(models.sale.Sale)
    if id_salesman:
        query = query.filter(models.sale.Sale.id_salesman == id_salesman)
    if id_store:
        query = query.filter(models.sale.Sale.id_store == id_store)
    if id_product:
        query = query.filter(models.sale.Sale.id_product == id_product)
    if date:
        query = query.filter(models.sale.Sale.date == date)
    return query.offset(skip).limit(limit).all()


def create_sale(db: Session, sale: schemas.sale.SaleCreate, id_salesman: int, id_store: int, id_product: int):
    db_sale = models.sale.Sale(**sale.dict(), id_salesman=id_salesman, id_store=id_store, id_product=id_product)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale
