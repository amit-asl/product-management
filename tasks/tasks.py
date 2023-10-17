from models.product import Product
from db import session
import json
from models.product import ProductModel



def create_product(name=None, price=None, category=None):
    current_product = Product(name=name, price=price, category=category)
    current_product.save()

def show_all_products():
    all_records = session.query(Product).all()
    all_records = [record.to_dict() for record in all_records]
    return json.dumps(all_records)

# This is for the post request ; pr denotes post request here
def create_product_task(product: ProductModel):
    current_product = Product(**product.model_dump())
    return current_product.save()

# this is for deleting a product
def delete_product_task(id: str):
    Product.delete(id)

# this is for updating a product
def update_product_task(id: str, payload: ProductModel):
    Product.update(id, payload.name, payload.price, payload.category)
