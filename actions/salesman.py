from sqlalchemy.orm import Session

import models
import schemas


def get_salesman(db: Session, dni: int):
    return db.query(models.salesman.Salesman).filter(models.salesman.Salesman.dni == dni).first()


def get_salesmen(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.salesman.Salesman).offset(skip).limit(limit).all()


def create_salesman(db: Session, salesman: schemas.salesman.SalesmanCreate):
    db_salesman = models.salesman.Salesman(name=salesman.name, dni=salesman.dni)
    db.add(db_salesman)
    db.commit()
    db.refresh(db_salesman)
    return db_salesman
