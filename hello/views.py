from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Special class to return the request 
    return render(request, "hello/index.html")

def broset(request):
    return HttpResponse("Hello broset!")

def greet(request, name):
    return render(request, "hello/greet.html", {
            "name": name.capitalize()
        })
