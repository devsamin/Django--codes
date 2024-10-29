from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This my first_app home page.")

def courses(request):
    return HttpResponse("This my first_app courses page.")

def about(request):
    return HttpResponse("This my first_app about page.")