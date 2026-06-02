from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ListingManagementTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username='admin-user',
            password='Password123',
            is_staff=True,
            is_superuser=True,
        )

    def test_invalid_sort_parameter_does_not_error(self):
        self.client.force_login(self.admin)

        response = self.client.get(
            reverse('listing_management'),
            {'sort': 'not-a-real-field'},
        )

        self.assertEqual(response.status_code, 200)
