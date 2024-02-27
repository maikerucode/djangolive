from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.viewFlights, name="index"),
    path("<int:flight_id>", views.indivFlight, name="flight"),
    path("add/<int:flight_id>", views.addPassenger, name="addPassenger"),
    path("flights_form/", views.flights_form, name="flights_form"),
    path("add_flight", views.add_flight, name="add_flight"),
    path("passenger_form/", views.passenger_form, name="passenger_form"),
    path("add_passenger", views.add_newPassenger, name="new_passenger")
]