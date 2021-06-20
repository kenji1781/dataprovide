from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HelloDjango")



# Create your views here.
