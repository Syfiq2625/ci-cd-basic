from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Project 9 API"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"id": 1, "name": "Test Item", "price": 10.5, "is_offer": True},
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

def test_read_item():
    # Setup: Create first
    client.post("/items/", json={"id": 2, "name": "Item 2", "price": 15.0})
    
    # Test Read
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2

def test_read_nonexistent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
