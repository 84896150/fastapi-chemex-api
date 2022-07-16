from typing import List, Optional

from pydantic import BaseModel
from datetime import date, datetime

class Admin_usersBase(BaseModel):
    name: str
    #lend_time: Optional[datetime] = None
    #lend_description: Optional[str] = None
    #plan_return_time: Optional[datetime] = None
    #return_time: Optional[datetime] = None
    #return_description: Optional[str] = None
    #deleted_at: Optional[datetime] = None
    #created_at: Optional[datetime] = None
    #updated_at: Optional[datetime] = None

class Admin_usersCreate(Admin_usersBase):
    pass


class Admin_users(Admin_usersBase):
    id: int
    #owner_id: int

    class Config:
        orm_mode = True





class Device_categoriesBase(BaseModel):
    name: str
    description: Optional[str] = None
    depreciation_rule_id: Optional[int] = None
    parent_id: Optional[int] = None
    order: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Device_categoriesCreate(Device_categoriesBase):
    pass


class Device_categories(Device_categoriesBase):
    id: int
    #owner_id: int

    class Config:
        orm_mode = True


class Device_tracksBase(BaseModel):
    #device_id: int
    #user_id: int
    user: List[Admin_users] = []
    #lend_time: Optional[datetime] = None
    #lend_description: Optional[str] = None
    #plan_return_time: Optional[datetime] = None
    #return_time: Optional[datetime] = None
    #return_description: Optional[str] = None
    #deleted_at: Optional[datetime] = None
    #created_at: Optional[datetime] = None
    #updated_at: Optional[datetime] = None


class Device_tracksCreate(Device_tracksBase):
    pass


class Device_tracks(Device_tracksBase):
    id: int
    #owner_id: int

    class Config:
        orm_mode = True



class Device_recordsBase(BaseModel):
    asset_number: str


class Device_recordsCreate(Device_recordsBase):
    password: str


class Device_records(Device_recordsBase):
    id: int
    name: str
    description: Optional[str] = None
    category: List[Device_categories] = []
    vendor: List[Device_tracks] = []
    #vendor_id: Optional[int] = None
    mac: Optional[str] = None
    ip: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[str] = None
    purchased: Optional[date] = None
    expired: Optional[date] = None
    depreciation_rule_id: Optional[int] = None
    #asset_number: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


