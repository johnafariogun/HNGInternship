import unittest
from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app instance
import os

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    
    def test_create_person(self):
        sample_person = {
            "name": "John Doe",
            "age": 30,
            "track": "Software Engineering",
            "slack_username": "johndoe"
        }
        
        response = self.client.post("/person/", json=sample_person)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue("id" in data)
        self.assertEqual(data["name"], sample_person["name"])
        self.assertEqual(data["age"], sample_person["age"])
        self.assertEqual(data["track"], sample_person["track"])
        self.assertEqual(data["slack_username"], sample_person["slack_username"])
    
    def test_read_person(self):
        name = "John Doe"
        response = self.client.get(f"/person/{name}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)
        person_data = data[0]
        self.assertEqual(person_data["name"], name)
    
    def test_update_person(self):
        person_id = 1  # Replace with an existing person ID
        updated_age = 35
        updated_data = {
            "name": "John Doe",
            "age": updated_age,
            "track": "Software Engineering",
            "slack_username": "johndoe"
        }
        response = self.client.put(f"/person/{person_id}", json=updated_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue("id" in data)
        self.assertEqual(data["name"], updated_data["name"])
        self.assertEqual(data["age"], updated_age)
        self.assertEqual(data["track"], updated_data["track"])
        self.assertEqual(data["slack_username"], updated_data["slack_username"])
    
    def test_delete_person(self):
        person_id = 1  # Replace with an existing person ID
        response = self.client.delete(f"/person/{person_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue("id" in data)
        # Add more assertions if needed for delete operation

if __name__ == "__main__":
    unittest.main()
