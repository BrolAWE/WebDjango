from django.urls import path

from .views import *

urlpatterns = [
    path('certificates/', certificates, name='certificates'),
    path('certificate/<pk>', certificate, name='certificate'),
    path('topic/<pk>', topic_details, name="topic_details"),
    path('research/', research, name='research'),
]
