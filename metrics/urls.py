from django.contrib import admin
from django.urls import path, include
from .views import graph1


urlpatterns = [
    path('graph1/', graph1),
]