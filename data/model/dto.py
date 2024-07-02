from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ApplicationStorageDto(Base):
    __tablename__ = 'application'

    id = Column(String, primary_key=True)
    counterparty = Column(String)
    car_plate = Column(String)
    operation_type = Column(String)
    equipment_type = Column(String)
    camera_type = Column(String, nullable=True)
    scales_type = Column(String, nullable=True)
    weight_gross = Column(String, nullable=True)
    weight_extra = Column(String, nullable=True)
    weight_container = Column(String, nullable=True)
    weight_net = Column(String, nullable=True)
    url_photo = Column(String, nullable=True)
    date = Column(String)
    end_weighing = Column(Boolean)


class EquipmentStorageDto(Base):
    __tablename__ = 'equipment'
    id = Column(String, primary_key=True)
    name = Column(String)

class OrderStorageDto(Base):
    __tablename__ = 'order'
    id = Column(String, primary_key=True)
    counterparty = Column(String)
    car_plate = Column(String)
    inn = Column(String)

