from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vehicle_fleet.models import Vehicle
from vehicle_fleet.views import VehicleViewSet, FuelTypeViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'fuel_types', FuelTypeViewSet, basename='fuel_types')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]
