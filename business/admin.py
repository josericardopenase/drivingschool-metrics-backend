from django.contrib import admin

from business.models import Section, DrivingLicense
from vehicle_fleet.models import FuelType

# Register your models here.
admin.site.register(Section)
admin.site.register(DrivingLicense)
admin.site.register(FuelType)