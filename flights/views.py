from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from .models import Airport, Flight,Passenger

# Create your views here.
def index(request):
    context={
        'flights':Flight.objects.all()
    }
    return render(request,'flights/index.html',context)

def flight(request,flight_id):
    try:
        flight=Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("flight does not exist")
    context={
        'flight':flight,
        'passengers':flight.passengers.all(),
        "non-passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render(request,"flights/flight.html",context)

def book(request,flight_id):
    try:
        passenger_id=int(request.POST["passenger"])
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request,"flights/error.html",{"message":"no selection"})
    except Flight.DoesNotExist:
        return render(request,"flights/error.html",{"message":"no flight"})
    except Passenger.DoesNotExist:
        return render(reques,"flights/error.html",{"message":"no passenger"})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))
