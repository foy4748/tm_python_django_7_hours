from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
rooms = [
        {
            "id":1, 
            "name":"JS Devs",
        },
        {
            "id":2, 
            "name":"Learn ReactJS",
        },
        {
            "id":3, 
            "name":"Mastering ExpressJS",
        },
        {
            "id":4, 
            "name":"MongoDB Advanced Features",
        },
]

def home(req):
    print(req.method)
    return render(req, 'base/home.html')

def room(req):
    return render(req, 'base/room.html', context={"rooms":rooms})
