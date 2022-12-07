from django.test import TestCase
from .models import Workshop

# This is a test to confirm, that the default model generates
# the right values for date, time and email respectively.


class TestModels(TestCase):

    def test_default_workshop(self):
        workshop = Workshop.objects.create(
            day='2022-12-07',
            time='6 PM',
            email='test@testmail.com'
        )
        self.assertEqual(workshop.day, '2022-12-07')
        self.assertEqual(workshop.time, '6 PM')
        self.assertEqual(workshop.email, 'test@testmail.com')
