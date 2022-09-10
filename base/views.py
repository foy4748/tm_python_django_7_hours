from django.shortcuts import render
#from django.http import HttpResponse

from .models import Room, Message

# Create your views here.

def home(req):
    rooms = Room.objects.all()
    return render(req, 'base/home.html', context={"rooms":rooms})

def room(req, pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room_id=pk)
    return render(req, 'base/room.html', context={"room":room, "messages":messages})

