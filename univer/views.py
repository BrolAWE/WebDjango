from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def db(request):
    return HttpResponse('alarm')
