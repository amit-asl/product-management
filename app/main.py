from datetime import datetime
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tasks.tasks import create_product, show_all_products, create_product_task, delete_product_task, update_product_task
from fastapi.responses import JSONResponse
import json
from models.product import ProductModel
import uuid
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

@app.get('/')
def test():
    return {
        'res': 'test'
    }

# DEMO
# @app.get('/{name}/{price}/{category}')
# def register_product(name, price, category):
#     create_product(name, price, category)

# CREATE
@app.post('/create_post')
async def register_post(product: ProductModel):
    product = create_product_task(product)
    return JSONResponse(json.dumps(product.to_dict()))

# RETRIEVE
@app.get('/get_products')
def show_products():
    return JSONResponse(json.loads(show_all_products()))

# UPDATE
@app.put('/product/update/{id}')
def update_product(id: str, payload: ProductModel):
    update_product_task(id, payload)

# DELETE
@app.delete('/product/delete/{id}')
def delete_product(id: str):
    id = uuid.UUID(id)
    delete_product_task(id)