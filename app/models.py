from sqlalchemy import Column, Integer, String
from app.database import Base

class BogieForm(Base):
    __tablename__ = "bogie_forms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    part_number = Column(String)

class WheelForm(Base):
    __tablename__ = "wheel_forms"
    id = Column(Integer, primary_key=True, index=True)
    inspector_name = Column(String)
    wheel_number = Column(String)
