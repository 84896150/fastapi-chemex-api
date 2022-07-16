from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Device_records(Base):
    __tablename__ = "device_records"

    id = Column(Integer, primary_key=True, index=True)
    #is_active = Column(Boolean, default=True)
    name = Column(String,unique=True, index=True)
    description = Column(String)
    category_id = Column(Integer)
    vendor_id = Column(Integer)
    mac = Column(String)
    ip = Column(String)
    photo = Column(String)
    price = Column(String)
    purchased = Column(String)
    expired = Column(String)
    depreciation_rule_id = Column(String)
    asset_number = Column(String)
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("Device_categories", back_populates="categorys")
    vendor = relationship("Device_tracks", back_populates="vendors")


class Device_categories(Base):
    __tablename__ = "device_categories"

    id = Column(Integer,  ForeignKey("device_records.category_id"),primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    depreciation_rule_id = Column(String)
    parent_id = Column(String)
    order = Column(String)
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    categorys = relationship("Device_records", back_populates="category")

class Device_tracks(Base):
    __tablename__ = "device_tracks"

    id = Column(Integer, ForeignKey("device_records.vendor_id"), primary_key=True, index=True)
    device_id = Column(Integer)
    user_id = Column(Integer)
    lend_time = Column(DateTime)
    lend_description = Column(String)
    plan_return_time = Column(String)
    return_time = Column(DateTime)
    return_description = Column(String)
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    vendors = relationship("Device_records", back_populates="vendor")
    user = relationship("Admin_users", back_populates="users")

class Admin_users(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, ForeignKey("device_tracks.user_id"), primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    avatar = Column(String)
    remember_token = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    department_id = Column(Integer)
    gender = Column(String)
    title = Column(String)
    mobile = Column(String)
    email = Column(String)
    ad_tag = Column(Integer)
    extended_fields = Column(String)
    deleted_at = Column(DateTime)
    status = Column(Integer)

    users = relationship("Device_tracks", back_populates="user")