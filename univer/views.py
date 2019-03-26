from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from univer.models import Dostopr


def db(request):
    return HttpResponse('go')


def stat(request):
    return render(request, 'index.html')


def postg(request):
    b = Dostopr.objects.all()
    print("hi")
    return render(request, "db.html", {"b": b})
