from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.db.models import Q

from .models import Room, Message, Topic
from .forms import RoomForm

# Create your views here.

def home(req):
    q = req.GET.get('q')

    if req.method == 'POST':
        q = req.POST.get('q')

    rooms = Room.objects.all()
    topics = Topic.objects.all()
    if q is not None:
        print(q)
        #rooms = Room.objects.filter(topic__name=q)
        #rooms = Room.objects.filter(topic__name__icontains=q)

        # Skim through the db.sqlite3 file then you will understand how to 
        # write these Q-filters 
        # foreignTable__foreignField__option  <<< That's the format
        rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q) | Q(host__username=q))

    return render(req, 'base/home.html', context={"rooms":rooms, "topics":topics})

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

def update_room(req, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    ctx = {"form":form}
    return render(req, 'base/room_form.html', context=ctx)

def delete_room(req, pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')

    return render(req, 'base/delete_room.html', context={'obj': room})
