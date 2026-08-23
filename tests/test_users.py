import pytest
from api.api_client import APIClient

#Create one client used by all tests
@pytest.fixture
def client():
    return APIClient()

# Test 1 — GET all users
def test_get_all_users(client):
    response= client.get("/users")
    assert response.status_code==200
    users = response.json()
    assert len(users)>0
    print(f"✅ Got {len(users)} users!")

# Test 2 — GET single user 
def test_get_single_user(client):
    response = client.get("/users/1") 
    assert response.status_code == 200 
    user = response.json() 
    assert user["id"] == 1 
    assert user["name"] == "Leanne Graham" 
    print(f"✅ Got user: {user['name']}")

# Test 3 — POST create new user 
def test_create_user(client): 
    new_user = { 
        "name": "Menna Bahaa", 
        "email": "menna@test.com", 
        "job": "QA Engineer" 
        } 
    response = client.post("/users", new_user) 
    assert response.status_code == 201 
    created = response.json() 
    assert created["name"] == "Menna Bahaa" 
    print(f"✅ Created user: {created['name']}")

# Test 4 — PUT update user 
def test_update_user(client): 
    updated_data = { 
        "name": "Menna Updated", 
        "email": "menna\_updated@test.com" 
        } 
    response = client.put("/users/1", updated_data) 
    assert response.status_code == 200 
    updated = response.json() 
    assert updated["name"] == "Menna Updated" 
    print(f"✅ Updated user: {updated['name']}")

# Test 5 — DELETE user 
def test_delete_user(client): 
    response = client.delete("/users/1") 
    assert response.status_code == 200 
    print("✅ User deleted successfully!") 

# Test 6 — GET non-existing user 
def test_get_missing_user(client): 
    response = client.get("/users/999") 
    assert response.status_code == 404 
    print("✅ Correctly returned 404 for missing user!")