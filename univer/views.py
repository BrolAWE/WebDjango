from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import TemplateView

from univer.models import Dostopr, Topic
from univer.storage import counter


def stat(request):
    return render_to_response('index.html')


def postg(request):
    b = Dostopr.objects.all()
    print("hi")
    return render(request, "db.html", {"b": b})


def jsdb(request):
    b = Dostopr.objects.values()
    list_result = [entry for entry in b]
    return JsonResponse(list_result, safe=False)


def topic_details(request, pk):
    try:
        topic=Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        raise Http404
    return render(request, 'topic_details.html',context={
        'topic': topic
    })


class IndexView(TemplateView):
    topics = Topic.objects.all()
    template_name = 'index.html'
    extra_context = {
        'topics': topics}

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['counter'] = counter.inc()
        return data
