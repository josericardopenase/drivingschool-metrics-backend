from django.contrib import admin
from django.urls import path, include
from .views import graph1,graph2,graph3


urlpatterns = [
    path('graph1/', graph1),
    path('graph2/', graph2),
    path('graph3/', graph3),

]