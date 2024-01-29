# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "appab/index.html")


def about(request):
    return render(request, "appab/about.html")

def services(request):
    return render(request, "appab/services.html")