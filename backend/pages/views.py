from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Django 'render' shortcut function that cna be used to create views
# however, there is a SIMPLER approach-- HttpResponse method

# Create your views here
# where we handle the request/response logic for our web app

def home_page_view(request):
    return HttpResponse("Hello world")
