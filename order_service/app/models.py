from sqlalchemy import Column, String, Integer
from .database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True)
    status = Column(String)