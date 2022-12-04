from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Workshop
from django.core.mail import send_mail
from .forms import AppointmentForm
import os


def workshop(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST['email']
        day = request.POST['day']
        time = request.POST['time']
        host = os.environ["EMAIL_HOST_USER"]

        booking_form = AppointmentForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.user = request.user
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
        user = request.user
        appointments = Workshop.objects.filter(user=user).order_by('day')
        return render(request, 'workshop.html', {
            "user": user,
            "appointments": appointments,
            "appointment_form": AppointmentForm(),
            "booked": False,
        })


class AppointmentRemove(View):

    def post(self, request, appointment_id, *args, **kwargs):
        workshop_to_remove = get_object_or_404(Workshop, id=appointment_id)
        workshop_to_remove.remove()

        return HttpResponseRedirect(reverse('workshop_list'))
