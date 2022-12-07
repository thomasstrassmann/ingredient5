from .models import Workshop
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ('day', 'time', 'email')
        widgets = {
            'day': DateInput(),
        }
