from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base
from .models import Product

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Sample in-memory "database"
inventory_data = {
    "A001": {"id": "A001", "name": "Laptop", "availability_status": "InStock"},
    "A002": {"id": "A002", "name": "Mouse", "availability_status": "OutOfStock"},
    "A003": {"id": "A003", "name": "Keyboard", "availability_status": "InStock"},
}

@app.get("/inventory/{product_id}")
async def get_product_availability(product_id: str):
    product = inventory_data.get(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")