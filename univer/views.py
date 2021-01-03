from django.db.models import Q, Max, Min
from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render

from univer.models import Dostopr


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
        if not up.isnumeric():
            up = Dostopr.objects.aggregate(Max(interval))[interval + '__max']
        if not down.isnumeric():
            down = Dostopr.objects.aggregate(Min(interval))[interval + '__min']
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


def mpro1(request):
    a = [float(i) for i in request.GET.get("a", "").split()]
    b = [float(i) for i in request.GET.get("b", "").split()]
    if a[0] > a[1] or len(a) != 2 or b[0] > b[1] or len(b) != 2:
        return HttpResponse("Error")
    if a[0] >= b[0] and a[1] <= b[1]:
        return HttpResponse("pervlvovt")
    elif b[0] >= a[0] and b[1] <= a[1]:
        return HttpResponse("vtorvlvperv")
    else:
        return HttpResponse("nevl")


def mpro2(request):
    f = []
    c = True
    a = int(request.GET.get("a", ""))
    if a <= 0:
        return HttpResponse("Error")
    while c:
        if a == 1:
            f.append(a)
            break
        for i in range(2, a + 1):
            if i == a:
                f.append(i)
                c = False
            elif a % i == 0:
                f.append(i)
                a = int(a / i)
                break
    return HttpResponse(str(f[0]))


def mpro3(request):
    import math
    f = []
    z = []
    a = int(request.GET.get("a", ""))
    if a <= 0:
        return HttpResponse("Error")
    for i in range(int(math.pow(10, a - 1)), int(9 * math.pow(10, a - 1) + 1)):
        if math.sqrt(i) % 1 == 0:
            f.append(i)
    for i in f:
        if str(i)[len(str(i)) - 1] == str(i)[len(str(i)) - 2]:
            z.append(i)
    return HttpResponse(z[len(z) - 1])


def mpro4(request):
    import random
    L = []
    S = 0
    K = 0
    for i in range(10):
        s = random.randint(10, 99)
        L.append(s)
        S += s
    S = S / 10
    L.sort()
    if S - L[0] > L[len(L) - 1] - S:
        return HttpResponse(str(L[0]))
    else:
        return HttpResponse(str(L[len(L) - 1]))


def mpro5(request):
    S = []
    a = int(request.GET.get("a", ""))
    if a <= 0 or a > 10:
        return HttpResponse("Error")
    for i in range(10, 100):
        if i % 9 == 0 or str(i)[1] == '5':
            S.append(i)
    return HttpResponse(str(S[a - 1]))
