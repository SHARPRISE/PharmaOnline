from django.test import TestCase
from .models import Medicament

from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class ViewTestCase(TestCase):
    """Test suite for the api views"""
    def setup(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.medicament_data = {'commercial': 'Aleve'}
        self.response = self.client.post(
            reverse('medicaments/ajouter'),
            self.medicament_data,
            format="json"
        )

    def can_create_medicament(self):
        """Test that the api has medicament creation capability"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def can_update_medicament(self):
        """Test that the api has medicament update capability"""
        change_medicament = {'commercial': 'Mucinex'}
        res = self.client.put(
            reverse('details', kwargs={'pk': medicament.id})
            change_medicament, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_medicament(self):
        """Test the api can get a given bucketlist."""
        medicament = Medicament.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': medicament.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, medicament)

    def test_api_can_delete_medicament(self):
        """Test the api can delete a bucketlist."""
        medicament = Medicament.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': medicament.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
