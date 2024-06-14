from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contacts = Column(Integer)
    location = Column(String)


    cars = relationship("Car", back_populates="seller")