from sqlalchemy.orm import Session

import models
import schemas


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.product.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.product.ProductCreate):
    db_product = models.product.Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
