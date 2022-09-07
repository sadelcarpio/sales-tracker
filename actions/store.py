from sqlalchemy.orm import Session

import models
import schemas


def get_store(db: Session, ruc_or_dni: int):
    return db.query(models.store.Store).filter(models.store.Store.ruc_or_dni == ruc_or_dni).first()


def get_stores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.store.Store).offset(skip).limit(limit).all()


def create_store(db: Session, store: schemas.store.StoreCreate):
    db_store = models.store.Store(ruc_or_dni=store.ruc_or_dni, name=store.name, lat=store.lat, long=store.long)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store
