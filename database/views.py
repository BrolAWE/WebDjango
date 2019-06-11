from django.db import connection
from django.db.models import Q, Max, Min
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django import db

# Create your views here.
from database.models import Dostopr


def postg(request):
    b = Dostopr.objects.all()
    return render(request, "db.html", {"b": b})


def jsdb(request):
    first = request.GET.get("first", "")
    second = request.GET.get("second", "")
    firstsearch = request.GET.get("firstsearch", "")
    howfirstsearch = request.GET.get("howfirstsearch", "")
    secondsearch = request.GET.get("secondsearch", "")
    howsecondsearch = request.GET.get("howsecondsearch", "")
    interval = request.GET.get("interval", "")
    down = request.GET.get("down", "")
    up = request.GET.get("up", "")
    li = [first, second]
    lis = []

    for i in li:
        if i != "":
            lis.append(i)

    if len(lis) == 0:
        if howfirstsearch != "":
            if howsecondsearch == "":
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}))
            else:
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}),
                                                    Q(**{'{0}__contains'.format(howsecondsearch): secondsearch}))
        else:
            b = Dostopr.objects.values()
    elif len(lis) == 1:
        if howfirstsearch != "":
            if howsecondsearch == "":
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}))
            else:
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}),
                                                    Q(**{'{0}__contains'.format(howsecondsearch): secondsearch}))
        else:
            b = Dostopr.objects.values().order_by(lis[0])
    elif len(lis) == 2:
        if howfirstsearch != "":
            if howsecondsearch == "":
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}))
            else:
                b = Dostopr.objects.values().filter(Q(**{'{0}__contains'.format(howfirstsearch): firstsearch}),
                                                    Q(**{'{0}__contains'.format(howsecondsearch): secondsearch}))
        else:
            b = Dostopr.objects.values().order_by(lis[0], lis[1])
    if interval != "":
        up=Dostopr.objects.aggregate(Max('rate'))['rate__max']
        b = Dostopr.objects.values().filter(Q(**{'{0}__range'.format(interval): (down, up)}))
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
        raise Http404
    return HttpResponse('')


def inbase(request):
    try:
        pk = int(request.GET.get("pk", ""))
        Dostopr.objects.get(pk=pk)
    except Dostopr.DoesNotExist:
        return HttpResponse("NoOK")
    return HttpResponse("OK")
