from sqlalchemy.orm import Session

import models
import schemas


def get_salesman_by_dni(db: Session, dni: int):
    return db.query(models.salesman.Salesman).filter(models.salesman.Salesman.dni == dni).first()


def get_salesmen(db: Session, namelike: str | None = None, skip: int = 0, limit: int = 10):
    query = db.query(models.salesman.Salesman)
    if namelike:
        query = query.filter(models.salesman.Salesman.name.like('%' + namelike + '%'))
    return query.offset(skip).limit(limit).all()


def create_salesman(db: Session, salesman: schemas.salesman.SalesmanCreate):
    db_salesman = models.salesman.Salesman(**salesman.dict())
    db.add(db_salesman)
    db.commit()
    db.refresh(db_salesman)
    return db_salesman
