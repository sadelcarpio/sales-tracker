from sqlalchemy.orm import Session

import models


def get_salesman_by_dni(db: Session, dni: str):
    return db.query(models.salesman.Salesman).filter(models.salesman.Salesman.dni == dni).first()


def get_salesmen(db: Session, namelike: str | None = None, skip: int = 0, limit: int = 10):
    query = db.query(models.salesman.Salesman)
    if namelike:
        query = query.filter(models.salesman.Salesman.name.like('%' + namelike + '%'))
    return query.offset(skip).limit(limit).all()
