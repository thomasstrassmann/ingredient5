from django.shortcuts import render
from django.views import View
from .models import Workshop
from django.core.mail import send_mail
from .forms import AppointmentForm
import os


def workshop(request):
    if request.method == 'POST':
        username = request.user.username
        email = request.POST['email']
        day = request.POST['day']
        time = request.POST['time']
        host = os.environ["EMAIL_HOST_USER"]

        send_mail(
            "Your virtual cooking workshop by Ingredient5",
            "Thanks for your reservation on the" + day + "at" + time,
            host,
            (email,))

        return render(request, 'workshop.html', {"appointment_form": AppointmentForm()})

    else:
        return render(request, 'workshop.html', {"appointment_form": AppointmentForm()})
