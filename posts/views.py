from django.shortcuts import render, HttpResponse
from random import randint

def index(requset):
    return HttpResponse(f"Hello world, {randint(0, 100)}")

def html_view(requset):
    return render(requset, "test.html")

# Create your views here.
