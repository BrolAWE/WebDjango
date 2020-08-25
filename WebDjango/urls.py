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
from django.contrib import admin
from django.urls import path, include
from core.univer_views import *

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('certificates/', certificates, name='certificates'),
    path('certificate/<pk>', certificate, name='certificate'),
    path('db/', postg, name='database'),
    path('jsdb/', jsdb),
    path('add/', add),
    path('delete/', delete),
    path('edit/', edit),
    path('inbase/', inbase),
    path('mpro1/', mpro1),
    path('mpro2/', mpro2),
    path('mpro3/', mpro3),
    path('mpro4/', mpro4),
    path('mpro5/', mpro5),
    path('topic/<pk>', topic_details, name="topic_details"),
    path('research/', research, name='research'),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
