from django.shortcuts import render
#from django.http import HttpResponse

from .models import Room

# Create your views here.

def home(req):
    rooms = Room.objects.all()
    return render(req, 'base/home.html', context={"rooms":rooms})

def room(req, pk):
    print(dir(Room.objects))
    room = Room.objects.filter(id=pk)[0]
    print(room)
    return render(req, 'base/room.html', context={"room":room})
