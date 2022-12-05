from django.shortcuts import render, reverse, get_object_or_404
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
            ("Thanks for your reservation on the " + day + " at "
                + time + ".\n"
                "We are really looking forward to create a great "
                "cooking class with you ant the other star chefs. \n"
                "What you should consider in any case: \n"
                "Have a fully charged smartphone/tablet ready for the "
                "appointment. \n"
                "We will email you the required ingredients 3 days in "
                "advance so that you still have the opportunity to go "
                "shopping. \n \n"

                "The google-meet link to the meeting: \n"
                "https://meet.google.com/fak-elo-gin \n \n"

                "In the attachment you will find the corresponding invoice. \n"
                "We are happy to have you and if you have any questions, "
                "please do not hesitate to contact us! \n \n"

                "Kind regards, \n"
                "your Ingredients Team"),
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
        workshop_to_remove.delete()

        return HttpResponseRedirect(reverse('workshop_list'))
