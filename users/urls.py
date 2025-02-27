from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from users.views import UserDetailView, IsAuthenticatedView


urlpatterns = [
    path('default/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('is_authenticated/', IsAuthenticatedView.as_view(), name='user-authenticated'),
]

