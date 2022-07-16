from sqlalchemy.orm import Session

from . import models, schemas


def get_asset_number(db: Session, asset_number_id: int):
    return db.query(models.Device_records).filter(models.Device_records.asset_number == asset_number_id).first()


def get_device(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Device_records).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Device_categories).offset(skip).limit(limit).all()


def get_admin_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Admin_users).offset(skip).limit(limit).all()

