from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request,"brandsurvey/index.html",({
        "questions":Question.objects.all(),
        "options":Option.objects.all(),
        "results":Result.objects.all(),
    }))

def thank(request):
    return render(request,"brandsurvey/thank.html")