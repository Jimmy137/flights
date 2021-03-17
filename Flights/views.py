from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def flights (request):
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all(), 
        
    })

def flight (request, id):
    flight = Flight.objects.get(id=id)
    pas = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "pass" : pas,
        "np" : Passenger.objects.exclude(flights= flight).all()
    })

def book (request, id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=id)
        p_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=p_id)
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("fl", args=[flight.id]))

