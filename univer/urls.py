from django.urls import path

from .views import *

urlpatterns = [
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
]
