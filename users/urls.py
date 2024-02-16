from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import UserProfileView, get_driving_school

urlpatterns = [
    path('default/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/school/', get_driving_school, name='user-profile-school'),
]
