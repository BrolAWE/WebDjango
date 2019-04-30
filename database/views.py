from django.http import JsonResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from database.models import Dostopr


def postg(request):
    b = Dostopr.objects.all()
    print("hi")
    return render(request, "db.html", {"b": b})


def jsdb(request):

    name = request.GET.get("name", "")
    latitude = request.GET.get("latitude", "")
    longitude = request.GET.get("longitude", "")
    rate = request.GET.get("rate", "")
    photo = request.GET.get("photo", "")
    li = [name, latitude, longitude, rate, photo]
    lis = []

    for i in li:
        if i != "":
            lis.append(i)

    if len(lis) == 0:
        b = Dostopr.objects.values()
    elif len(lis) == 1:
        b = Dostopr.objects.values().order_by(lis[0])
    elif len(lis) == 2:
        b = Dostopr.objects.values().order_by(lis[0], lis[1])
    elif len(lis) == 3:
        b = Dostopr.objects.values().order_by(lis[0], lis[1], lis[0])
    elif len(lis) == 4:
        b = Dostopr.objects.values().order_by(lis[0], lis[1], lis[2], lis[3])
    elif len(lis) == 5:
        b = Dostopr.objects.values().order_by(lis[0], lis[1], lis[2], lis[3], lis[4])
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
        dostopr = Dostopr.objects.get(pk=pk)
        dostopr.name = request.GET.get("name", "")
        dostopr.longitude = request.GET.get("longitude", "")
        dostopr.latitude = request.GET.get("latitude", "")
        dostopr.rate = request.GET.get("rate", "")
        dostopr.photo = request.GET.get("photo", "")
        dostopr.save()
    except Dostopr.DoesNotExist:
        return HttpResponseNotFound("<h2>Dostopr not found</h2>")
    return HttpResponse('')
