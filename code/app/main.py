from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# device查询
@app.get("/device/", response_model=List[schemas.Device_records])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_device(db, skip=skip, limit=limit)
    return items

# 根据资产卡片查询
@app.get("/device/{asset_number_id}", response_model=schemas.Device_records)
def read_items(asset_number_id: int, db: Session = Depends(get_db)):
    items = crud.get_asset_number(db, asset_number_id=asset_number_id)
    if items is None:
        raise HTTPException(status_code=404, detail="资产卡片未找到")
    return items

# 查询分类
@app.get("/device_categories/", response_model=List[schemas.Device_categories])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# 查询用户
@app.get("/users/", response_model=List[schemas.Admin_users])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_admin_users(db, skip=skip, limit=limit)
    return items