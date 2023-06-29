import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "apple"})
    assert response.status_code == 200
    assert response.json()["name"] == "apple"
    assert response.json()["item_id"] is not None

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item():
    response = client.post("/items/", json={"name": "banana"})
    item_id = response.json()["item_id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "banana"

def test_delete_item():
    response = client.post("/items/", json={"name": "orange"})
    item_id = response.json()["item_id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["error"] == "Item not found"