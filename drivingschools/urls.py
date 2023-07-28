from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrivingSchoolViewSet, DrivingPermissionViewSet, DrivingSchoolSectionViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'schools', DrivingSchoolViewSet)
router.register(r'permissions', DrivingPermissionViewSet)
router.register(r'sections', DrivingSchoolSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]