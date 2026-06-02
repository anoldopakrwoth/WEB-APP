from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import ProduceListing


class CreateListingValidationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='farmer',
            password='Password123',
        )
        self.valid_payload = {
            'title': 'Fresh Tomatoes',
            'description': 'Good quality tomatoes',
            'price': '5000.00',
            'quantity': '1 crate',
            'village_origin': 'Mukono',
            'target_town': 'Kampala',
        }

    def test_invalid_price_does_not_create_listing(self):
        self.client.force_login(self.user)
        payload = {**self.valid_payload, 'price': 'not-a-number'}

        response = self.client.post(reverse('create_listing'), payload)

        self.assertRedirects(response, reverse('create_listing'))
        self.assertFalse(ProduceListing.objects.exists())

    def test_invalid_image_type_does_not_create_listing(self):
        self.client.force_login(self.user)
        upload = SimpleUploadedFile(
            'not-image.txt',
            b'plain text',
            content_type='text/plain',
        )
        payload = {**self.valid_payload, 'image': upload}

        response = self.client.post(reverse('create_listing'), payload)

        self.assertRedirects(response, reverse('create_listing'))
        self.assertFalse(ProduceListing.objects.exists())
