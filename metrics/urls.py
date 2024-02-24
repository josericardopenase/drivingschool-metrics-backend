from django.contrib import admin
from django.urls import path, include
from .views import autoescuelas_con_mas_presentados, graph1,graph2,graph3,graph4


urlpatterns = [
    path('graph1/', graph1),
    path('graph2/', graph2),
    path('graph3/', graph3),
    path('graph4/', graph4),
    path('more_presenteds/', autoescuelas_con_mas_presentados),
]