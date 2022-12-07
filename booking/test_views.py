from django.test import TestCase
from .models import Workshop


class TestViews(TestCase):

    def test_get_booking_page(self):
        response = self.client.get('/workshop/')
        self.assertEqual(response.status_code, 302)
