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
