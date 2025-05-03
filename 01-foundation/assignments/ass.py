"""Module providing a function printing python version."""
from pydantic import BaseModel

# TODO: create product model with id, name, price, in_stock

class Product(BaseModel):
    """Product representing a person"""
    id: str
    name: str
    price: int
    in_stock: bool


product_data = {"id": "102", "name": "some", "price": 20, "in_stock": True}

product = Product(**product_data)
print(product)
