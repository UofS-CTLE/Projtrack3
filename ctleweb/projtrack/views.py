from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello, CTLE!")
