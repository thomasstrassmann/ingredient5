from django.test import TestCase
from .forms import DateInput, AppointmentForm


class TestAppointmentForm(TestCase):

    def test_day_is_required(self):
        form = AppointmentForm({'day': '', 'time': '6 PM',
                                'email': 'test@testmail.com'})
        self.assertFalse(form.is_valid())

    def test_time_is_required(self):
        form = AppointmentForm({'day': '2022-12-07', 'time': '',
                                'email': 'test@testmail.com'})
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        form = AppointmentForm({'day': '2022-12-07', 'time': '6 PM',
                                'email': ''})
        self.assertFalse(form.is_valid())
