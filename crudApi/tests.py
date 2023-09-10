import requests
import json
import pytest


# Set the base URL for your API
BASE_URL = 'http://localhost:5000'

# Function to send a POST request to create a new person
def create_person(name, age, slack_username, track):
    data = {"name": name, "age": age, "slack_username": slack_username, "track": track}
    response = requests.post(f"{BASE_URL}/person", json=data)
    return response

# Function to send a GET request to retrieve a person by name
def get_person(name):
    response = requests.get(f"{BASE_URL}/person/{name}")
    return response

# Function to send a PUT request to update a person's details
def update_person(name, new_age, new_track):
    data = {"age": new_age, "track": new_track}
    response = requests.put(f"{BASE_URL}/person/{name}", json=data)
    return response

# Function to send a DELETE request to remove a person by name
def delete_person(name):
    response = requests.delete(f"{BASE_URL}/person/{name}")
    return response

# Test the API
if __name__ == '__main__':
    # Create a new person
    response = create_person("Alice", 28, "alice_is_golden", "backend")
    print("Create Person Response:")
    response = create_person("John", 20, "John_Tolulope_Afariogun", "frontend")
    print("Create Person Response:")
    print(response.json())

    # Retrieve a person by name
    response = get_person("Alice")
    print("Get Person Response:")
    print(response.json())

    # Update a person's details
    response = update_person("Alice", 29, "frontend")
    print("Update Person Response:")
    print(response.json())

    # Delete a person by name
    response = delete_person("Alice")
    print("Delete Person Response:")
    print(response.json())



# Set the base URL for your API
BASE_URL = 'http://localhost:5000'  # Update with your API's URL

# Define test cases
def test_create_person():
    # Test creating a new person
    data = {"name": "John", "age": 21, "slack_username": "John_Tolulope_Afariogun", "track": "backend"}
    response = requests.post(f"{BASE_URL}/person", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_get_person_by_name():
    # Test retrieving a person by name
    response = requests.get(f"{BASE_URL}/person/John Doe")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_update_person():
    # Test updating a person's age
    data = {"age": 31}
    response = requests.put(f"{BASE_URL}/person/John Doe", json=data)
    assert response.status_code == 200
    assert response.json()["age"] == 31

def test_delete_person():
    # Test deleting a person
    response = requests.delete(f"{BASE_URL}/person/John Doe")
    assert response.status_code == 200

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
