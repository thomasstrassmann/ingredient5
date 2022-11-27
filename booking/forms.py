from .models import Workshop
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ('day', 'time', 'email')