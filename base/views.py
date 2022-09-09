#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    print(req.method)
    html = '''
    <h1> Testing: HOME Page</h1>
    '''
    return HttpResponse(html)

def room(req):
    print(req.method)
    html = '''
    <h1> Testing: ROOM Page</h1>
    '''
    return HttpResponse(html)
