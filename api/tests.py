from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Bucketlist


# Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .factories import  BucketListFactory, UserFactory

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        user = UserFactory()
        BucketListFactory(name='Cool developer', owner=user)
        BucketListFactory(name='Java developer',owner=user)
        #BucketListFactory(name='Mobile apps programmer')
        #BucketListFactory(name='Intern developer Java')

        """Define the test client and other test variables."""
        self.client = APIClient()
        self.client.force_authenticate(user=user)


    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_bucketlists(self):
        """Test the api can get a given bucketlist."""
        response = self.client.get(
            reverse('create') , {'title': 'developer'}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print (response)


    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get(id=1)
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.first()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.first()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)