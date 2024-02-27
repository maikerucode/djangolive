from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from datetime import datetime
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "index/index.html")

def timeDisplay(request):
    time = datetime.now().time()
    return HttpResponse(f"Current Time: {time}")

def introduction(request, name):

    if name == " " or name == None:
        name = "twitch.tv/maikonshu"

    return render(request, "index/index.html", {
        "name" : name.capitalize()
    })

listMen = ["Carlos", "Ainz", "Asuka"]

def swetch(request):
    return render(request, "index/synchro.html", {
        "men" : listMen
    })