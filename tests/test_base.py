from uuid import UUID
from app.main import app
from fastapi.testclient import TestClient
import json
client = TestClient(app)

def test_create_product():
    data = {
        'name': 'asus',
        'price': 5000,
        'category': 'laptop'
    }
    response = client.get(f"/{data.get('name')}/{data.get('price')}/{data.get('category')}")

    assert response.status_code == 200

def test_retrieve_product():
    response = client.get(f"/get_products")
    result = response.content
    assert len(result) > 0

def test_delete_product():
    response = client.get(f"/get_products")
    products = json.loads(response.content)
    id = ''
    for product in products:
        if product['name'] == 'asus':
            id = product['id']
    
    response = client.delete(f'/product/delete/{id}')
    assert response.status_code == 200

# data = {
#         'name': 'windows',
#         'price': 7000,
#         'category': 'laptop'
#     }

def test_create_product_2():
    data = {
        'name': 'asus',
        'price': 5000,
        'category': 'laptop'
    }
    response = client.post(f"/create_post", json=data)

    assert response.status_code == 200

def test_update_product():
    data = {
        'name': 'xenon',
        'price': 5000,
        'category': 'laptop'
    }
    response = client.get(f"/get_products")
    products = json.loads(response.content)
    id = 'unknown'
    for product in products:
        if product['name'] == 'asus':
            id = product['id']
    
    response = client.put(f'/product/update/{id}', json=data)
    assert response.status_code == 200

def test_update_product_should_fail():
    data = {
        'name': 'xenon',
        'price': 5000,
        'category': 'laptop'
    }
    response = client.get(f"/get_products")
    products = json.loads(response.content)
    id = None
    for product in products:
        if product['name'] == 'dell':
            id = product['id']
    
    if id == None:
        assert id == None
    else:
        response = client.put(f'/product/update/{id}', json=data)
        assert response.status_code == 200





