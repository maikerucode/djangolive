from django.forms import ModelForm
from flights.models import Flight, Passenger


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        # fields = ['origin', 'destination', 'duration']
        fields = '__all__'

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'