from django import forms
from .models import Flight,Booking

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'