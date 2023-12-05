from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(response):
    return HttpResponse("This is first_app page");

def courses(response):
    return HttpResponse("This is course page");

def about(response):
    return HttpResponse("This is about page");
