from django.contrib import admin

from human_resources.models import Teacher, Employee, EmployeeSoftwareAccount, EmployeeSoftware, Administrative, \
    Contract, Payroll,Absence, Vacation

# Register your models here.
admin.site.register(Employee)
admin.site.register(Teacher)
admin.site.register(Administrative)
admin.site.register(EmployeeSoftwareAccount)
admin.site.register(EmployeeSoftware)

class ContractAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_active', 'hours_a_week')
    list_filter = ('is_active',)
    ordering = ('date',)

admin.site.register(Contract, ContractAdmin)

class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date')
    list_filter = ('date',)
    ordering = ('date',)

admin.site.register(Payroll, PayrollAdmin)

class VacationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'init_date', 'end_date')

admin.site.register(Vacation, VacationAdmin)

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'init_date', 'end_date')

admin.site.register(Absence, AbsenceAdmin)
