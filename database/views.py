from django.http import JsonResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from database.models import Dostopr


def postg(request):
    b = Dostopr.objects.all()
    print("hi")
    return render(request, "db.html", {"b": b})


def jsdb(request):
    sort = request.GET.get("sort", "")
    b = Dostopr.objects.values().order_by("name","latitude","longitude","rate","photo")
    list_result = [entry for entry in b]
    return JsonResponse(list_result, safe=False)


def delete(request):
    pk = request.GET.get("id", "")
    try:
        Dostopr.objects.get(pk=pk)
    except Dostopr.DoesNotExist:
        raise Http404
    Dostopr.objects.get(pk=pk).delete()
    return HttpResponse('')


def add(request):
    name = request.GET.get("name", "")
    longitude = request.GET.get("longitude", "")
    latitude = request.GET.get("latitude", "")
    rate = request.GET.get("rate", "")
    photo = request.GET.get("photo", "")
    Dostopr(name=name, longitude=longitude, latitude=latitude, rate=rate, photo=photo).save()
    return HttpResponse('')


def edit(request):
    try:
        pk = request.GET.get("id", "")
        dostopr=Dostopr.objects.get(pk=pk)
        dostopr.name = request.GET.get("name", "")
        dostopr.longitude = request.GET.get("longitude", "")
        dostopr.latitude = request.GET.get("latitude", "")
        dostopr.rate = request.GET.get("rate", "")
        dostopr.photo = request.GET.get("photo", "")
        dostopr.save()
    except Dostopr.DoesNotExist:
        return HttpResponseNotFound("<h2>Dostopr not found</h2>")
    return HttpResponse('')
