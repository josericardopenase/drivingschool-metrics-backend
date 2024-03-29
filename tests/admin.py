
from itertools import count
from django.contrib import admin
from .models import Test, TestCenter, TestType
from django.contrib import admin
from collections import Counter
# Assuming all models are in the same app, if not adjust the import paths accordingly


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_center', 'test_type', 'permission_type', 'school_section', 'month', 'year', 'num_aptos', 'num_presentados', 'num_suspensos')
    list_filter = ('test_center__province', 'school_section__driving_school', 'month', 'year', 'test_type', 'permission_type')
    search_fields = ('test_center__name', 'test_type__name', 'permission_type__name', 'school_section__driving_school__name')
    ordering = ('year', 'month')

admin.site.register(Test, TestAdmin)

admin.site.register(TestCenter)


admin.site.register(TestType)
