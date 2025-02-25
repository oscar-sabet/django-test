from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    
    if request.method == "GET":
        return HttpResponse(request.method)
        return HttpResponse("This was a GET request")
    elif request.method == "POST":
        
        return HttpResponse("This was a POST request")
        return HttpResponse("Hello, world. You're at the polls index.")
