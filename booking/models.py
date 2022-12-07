from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


TIME_SLOTS = (
    ("5 PM", "5 PM"),
    ("6:30 PM", "6:30 PM"),
    ("8 PM", "8 PM"),
)


class Workshop(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    day = models.DateField(default=datetime.now, null=False, blank=False)
    time = models.CharField(max_length=8, choices=TIME_SLOTS, default="5 PM",
                            null=False, blank=False)
    registered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user} booked on day {self.day} at {self.time}"
