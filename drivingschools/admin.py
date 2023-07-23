from django.contrib import admin
from .models import DrivingSchool, DrivingSchoolSection, DrivingPermission

# Register your models here.
admin.site.register(DrivingSchool)
admin.site.register(DrivingSchoolSection)
admin.site.register(DrivingPermission)
