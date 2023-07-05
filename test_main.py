import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    items.clear()  # Clear the in-memory storage before each test
    return TestClient(app)


def test_list_items_empty(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {}


def test_list_item_not_found(client):
    response = client.get("/items/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_add_item(client):
    response = client.post("/items", json={"item": "Eggs"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": "Eggs"}


def test_list_item(client):
    client.post("/items", json={"item": "Eggs"})
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "item": "Eggs"}


def test_delete_item(client):
    client.post("/items", json={"item": "Eggs"})
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"result": "Item deleted"}


def test_delete_item_not_found(client):
    response = client.delete("/items/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}