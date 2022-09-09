from sqlalchemy.orm import Session

import models
import schemas


def get_sales(db: Session, id_salesman: int | None = None, id_store: int | None = None, id_product: int | None = None,
              skip: int = 0, limit: int = 10):
    if id_salesman:
        return db.query(models.sale.Sale).filter(models.sale.Sale.id_salesman == id_salesman).all()
    elif id_store:
        return db.query(models.sale.Sale).filter(models.sale.Sale.id_store == id_store).all()
    elif id_product:
        return db.query(models.sale.Sale).filter(models.sale.Sale.id_product == id_product).all()
    return db.query(models.sale.Sale).offset(skip).limit(limit).all()


def create_sale(db: Session, sale: schemas.sale.SaleCreate, id_salesman: int, id_store: int, id_product: int):
    db_sale = models.sale.Sale(**sale.dict(), id_salesman=id_salesman, id_store=id_store, id_product=id_product)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale
