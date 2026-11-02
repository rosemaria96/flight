from django.shortcuts import render,redirect,get_object_or_404

from .models import Flight,Booking
from .forms import FlightForm, BookingForm
# Create your views here.
from decouple import config
import requests

API_KEY = config('FLIGHT_API_KEY')


def flight_api(request):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": "Kochi",
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return render(request, 'flights.html', {'data': data})

def home(request):

    search = request.GET.get('search')
    if search:
        flights = Flight.objects.filter(destination__icontains = search)
    else:
        flights = Flight.objects.all()

    return render(request, 'home.html',
                    {'flights': flights})

def add_flight(request):
    form = FlightForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add_flight.html', 
                  {'form': form})

def update_flight(request,id):
    flight = get_object_or_404(Flight,id=id)
    form = FlightForm(request.POST or None, instance = flight)

    if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'update_flight.html', 
                      {'form': form})

def delete_flight(request,id):
    flight = get_object_or_404(Flight, id=id)
    flight.delete()
    return redirect('home')

def book_flight(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
         
    return render(request, 'book_flight.html', 
                  {'form': form})