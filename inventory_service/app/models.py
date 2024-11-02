from sqlalchemy import Column, String, Integer
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    availability_status = Column(String)
