from django.shortcuts import render
from django.http import HttpResponse

def registrations(request):
    return HttpResponse('annyeong haseyo')

def school(request):
    return HttpResponse('university of mars')

def birthdate(request):
    return HttpResponse('february 31')

# Create your views here.
