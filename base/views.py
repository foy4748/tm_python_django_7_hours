from django.shortcuts import render, redirect
#from django.http import HttpResponse

from .models import Room, Message
from .forms import RoomForm

# Create your views here.

def home(req):
    rooms = Room.objects.all()
    return render(req, 'base/home.html', context={"rooms":rooms})

def room(req, pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room_id=pk)
    return render(req, 'base/room.html', context={"room":room, "messages":messages})

def create_room(req):
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    ctx = {'form': RoomForm}
    return render(req, 'base/room_form.html', context=ctx)
