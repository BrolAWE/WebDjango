from django.http import JsonResponse, Http404, HttpResponse
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


def delete(request, pk):
    try:
        Dostopr.objects.get(pk=pk)
    except Dostopr.DoesNotExist:
        raise Http404
    Dostopr.objects.get(pk=pk).delete()
    return HttpResponse('')


def add(request, name, longitude, latitude, rate, photo):
    Dostopr(name=name, longitude=longitude, latitude=latitude, rate=rate, photo=photo).save()
    return HttpResponse('')
