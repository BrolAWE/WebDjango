from django.http import Http404
from django.shortcuts import render

from core.models import Topic, Sertificat
from core.storage import counter


def topic_details(request, pk):
    """Представление новости"""
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'topic_details.html', context={
        'topic': topic,
    })


def index(request):
    """Представление главной страницы"""
    topics = Topic.objects.all()
    cou = counter.inc()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, "index.html", {"topics": topics,
                                                    "cou": cou,
                                                    'num_visits': num_visits
                                                              })


def certificates(request):
    """Представление сертификатов"""
    certificates = Sertificat.objects.all()
    return render(request, 'certificates.html', context={
        "certificates": certificates
    })


def certificate(request, pk):
    """Представление сертификата"""
    certificate = Sertificat.objects.get(pk=pk)
    return render(request, 'certificate.html', context={
        "certificate": certificate
    })


def research(request):
    """Представление исследования"""
    return render(request, 'research.html')
