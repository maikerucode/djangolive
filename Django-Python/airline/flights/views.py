from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Airport, Passenger
from .forms import FlightForm, PassengerForm

def viewFlights(request):

    flights = Flight.objects.all()

    return render(request, "index.html", {
        "flights" : flights
    })

def indivFlight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    allPassengers = Passenger.objects.exclude(flights=flight).all()

    return render(request, "flight.html", {"flight" : flight, "passengers" : passengers, "all_passengers" : allPassengers})

def addPassenger(request, flight_id):

    if request.method == "POST":
        # get current flight based on current page
        flight = Flight.objects.get(pk=flight_id)
        # get current passenger based on input from form
        passenger_id = request.POST["add_passenger"]
        # get specific passenger from all passengers through input
        passenger = Passenger.objects.get(pk=passenger_id)
        # add current flight to specified passenger
        passenger.flights.add(flight)
        # redirect to same page 
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

def flights_form(request):

    return render(request, "flights_form.html", {"form" : FlightForm()})

def add_flight(request):

    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            
            return  HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flights_form.html", {"form" : form})

def passenger_form(request):

    return render(request, "passenger_form.html", {"form" : PassengerForm()})

def add_newPassenger(request):

    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "passenger_form.html", {"form" : form})
