from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from database.models import Dostopr


def postg(request):
    b = Dostopr.objects.all()
    print("hi")
    return render(request, "db.html", {"b": b})


def jsdb(request):
    b = Dostopr.objects.values()
    list_result = [entry for entry in b]
    return JsonResponse(list_result, safe=False)