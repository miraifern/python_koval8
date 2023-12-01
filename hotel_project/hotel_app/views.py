from django.shortcuts import render
from .models import Guest, Room, Registration

def hotel_info(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    registrations = Registration.objects.all()

    return render(request, 'hotel_info.html', {'guests': guests, 'rooms': rooms, 'registrations': registrations})
