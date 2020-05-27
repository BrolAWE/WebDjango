from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, render_to_response

from django.db.models import Q, Max, Min
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from core.models import Topic, Sertificat
from core.storage import counter


def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'main_page/topic_details.html', context={
        'topic': topic,
    })


def index(request):
    topics = Topic.objects.all()
    cou = counter.inc()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, "main_page/index.html", {"topics": topics,
                                                    "cou": cou,
                                                    'num_visits': num_visits
                                                    })


def certificates(request):
    certificates = Sertificat.objects.all()
    return render(request, 'certificates.html', context={
        "certificates": certificates
    })


def certificate(request, pk):
    certificate = Sertificat.objects.get(pk=pk)
    return render(request, 'certificate.html', context={
        "certificate": certificate
    })
