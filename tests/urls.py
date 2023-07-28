# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestCenterViewSet, TestTypeViewSet, TestViewSet

router = DefaultRouter()
router.register(r'centers', TestCenterViewSet)
router.register(r'types', TestTypeViewSet)
router.register(r'', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]