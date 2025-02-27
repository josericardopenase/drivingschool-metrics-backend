from django.contrib import admin

from administrative_management.models import Student, Language, LeadSource, RegistrationState, Registration, \
    MedicalCertificate, RegistrationStateLog, TheoryAppRenovations
from administrative_management.models import (
    FollowingPlan,
    FollowingSchedule,
    FollowingForm,
    Following,
    FollowingTask,
    FollowingLog
)

# Register your models here.
admin.site.register(Student)
admin.site.register(Language)
admin.site.register(LeadSource)
admin.site.register(MedicalCertificate)

@admin.register(TheoryAppRenovations)
class TheoryAppRenovationsAdmin(admin.ModelAdmin):
    list_display = ('registration', 'date')

@admin.register(RegistrationStateLog)
class RegistrationLogAdmin(admin.ModelAdmin):
    list_display = ('registration', 'date_added', 'state')

@admin.register(Registration)
class RegistrationStateAdmin(admin.ModelAdmin):
    list_display = ('student', 'access_to_tests_expire_date', 'has_theorical_exam_pass', 'is_active')
    list_editable = ()  # Esto permite editar el campo directamente desde la lista

@admin.register(RegistrationState)
class RegistrationStateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_editable = ()  # Esto permite editar el campo directamente desde la lista


from django.contrib import admin

@admin.register(FollowingPlan)
class FollowingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('id',)

@admin.register(FollowingSchedule)
class FollowingScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'following', 'task_type', 'loop', 'days_since_register', 'repeat_every_days')
    list_filter = ('loop',)
    search_fields = ('name', 'task_type__name')

@admin.register(FollowingForm)
class FollowingFormAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'description')
    search_fields = ('type', 'name')

admin.site.register(Following)

@admin.register(FollowingTask)
class FollowingTaskAdmin(admin.ModelAdmin):
    list_display = ( 'timestamp', 'form')
    list_filter = ('timestamp', 'form')
    search_fields = ('form__name',)

@admin.register(FollowingLog)
class FollowingLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'registration', 'done_by')
    list_filter = ('timestamp',)
    search_fields = ()
