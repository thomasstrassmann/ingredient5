from . import views
from django.urls import path


urlpatterns = [
    path('workshop/', views.workshop, name='workshop_list'),
    path('workshop/<int:appointment_id>', views.AppointmentRemove.as_view(),
         name='remove_appointment'),
]
