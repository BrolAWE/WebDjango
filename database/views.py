from django.http import JsonResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from database.models import Dostopr


def postg(request):
    b = Dostopr.objects.all()
    return render(request, "db.html", {"b": b})


def jsdb(request):
    first = request.GET.get("first", "")
    second = request.GET.get("second", "")
    search = request.GET.get("search", "")
    howsearch = request.GET.get("howsearch", "")
    li = [first, second]
    lis = []

    for i in li:
        if i != "":
            lis.append(i)

    if len(lis) == 0:
        if howsearch != "":
            b = Dostopr.objects.values().eval("qs.filter(Q({}__contains={})".format(howsearch, search))
        else:
            b = Dostopr.objects.values()
    elif len(lis) == 1:
        if howsearch != "":
            b = Dostopr.objects.values().order_by(lis[0]).eval("qs.filter(Q({}__contains={})".format(howsearch, search))
        else:
            b = Dostopr.objects.values().order_by(lis[0])
    elif len(lis) == 2:
        if howsearch != "":
            b = Dostopr.objects.values().order_by(lis[0], lis[1]).eval(
                "qs.filter(Q({}__contains={})".format(howsearch, search))
        else:
            b = Dostopr.objects.values().order_by(lis[0], lis[1])
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
