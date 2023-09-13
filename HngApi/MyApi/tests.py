from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person
from .serializers import PersonSerializer

class PersonAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            "name": "John Doe",
            "track": "Backend",
            "slack_username": "johndoe",
            "email": "john.doe@example.com"
        }
        self.person = Person.objects.create(**self.person_data)
        self.url = reverse('person-list-create')

    def test_create_person(self):
        response = self.client.post(self.url, self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_person(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming you have at least one person in the database.

    def test_update_person(self):
        updated_data = {
            "name": "Updated Name",
            "track": "Updated Track",
            "slack_username": "updated_username",
            "email": "updated@example.com"
        }
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.name, updated_data["name"])
        self.assertEqual(self.person.track, updated_data["track"])

    def test_delete_person(self):
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Person.objects.filter(pk=self.person.id).exists())
