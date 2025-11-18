from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('HELLO WORLD')
def schedule(request):
    schedule = '1:00 - 5:00'
    return HttpResponse('MWF {schedule},TTH')
def sub(request):
    schedule = 'sub'
    return HttpResponse('ayaw ko ng math')

# Create your views here.
