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

        booking_form = AppointmentForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.username = request.user.username
            booking = booking_form.save(commit=False)
            booking.save()
        else:
            booking_form = AppointmentForm()

        send_mail(
            "Your virtual cooking workshop by Ingredient5",
            "Thanks for your reservation on the" + day + "at" + time,
            host,
            (email,))

        return render(
            request, 'workshop.html', {
                "appointment_form": AppointmentForm(),
                "booked": True})

    else:
        return render(
            request, 'workshop.html', {
                "appointment_form": AppointmentForm(),
                "booked": False})
