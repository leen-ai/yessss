from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    return HttpResponse('nihao')

def name(request):
    name = 'lauren'
    return HttpResponse(f'my name is {name}')

def id(request):
    id = '099909'
    return HttpResponse(f'my id is {id}')

# Create your views here.
