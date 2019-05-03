from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView

from univer.models import Topic
from univer.storage import counter


def topic_details(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'topic_details.html', context={
        'topic': topic,
    })


def index(request):
    topics = Topic.objects.all()
    cou = counter.inc()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, "index.html", {"topics": topics,
                                          "cou": cou,
                                          'num_visits': num_visits
                                          })

