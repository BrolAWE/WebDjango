"""WebDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from chat import views as chat_views
from database.views import postg, jsdb

from univer.views import IndexView, topic_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('db/', postg, name='database'),
    path('jsdb/', jsdb),
    url(r'^topic/(?P<pk>\d+)/$', topic_details, name="topic_details"),
    url(r'^chat/', include('chat.urls')),
    url(r'^$', chat_views.index),
]
