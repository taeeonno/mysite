from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow, world")
# Create your views here.
