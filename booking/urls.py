from . import views
from django.urls import path


urlpatterns = [
    path('workshop/', views.workshop, name='workshop_list'),
]
