from django.urls import path, include
from rest_framework.routers import DefaultRouter

from business.views import SectionViewSet, DrivingLicenseViewSet

router = DefaultRouter()
router.register(r'sections', SectionViewSet, basename='sections')
router.register(r'driving_licenses', DrivingLicenseViewSet, basename='driving_license')


urlpatterns = [
    path('', include(router.urls)),
]
