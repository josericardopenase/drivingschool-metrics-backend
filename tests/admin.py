from django.contrib import admin
from .models import Test, TestCenter, TestType

# Register your models here.
admin.site.register(Test)
admin.site.register(TestCenter)
admin.site.register(TestType)
