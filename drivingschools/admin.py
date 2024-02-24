from django.contrib import admin
from .models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from django.contrib import admin
from .models import DrivingSchool, DrivingSchoolSection, DrivingPermission

@admin.register(DrivingSchool, DrivingPermission)
class DefaultAdmin(admin.ModelAdmin):
    pass

@admin.register(DrivingSchoolSection)
class DrivingSchoolSectionAdmin(admin.ModelAdmin):
    # Mostrar estos campos en la lista de secciones
    list_display = ('code', 'zone', 'driving_school', 'name')

    # Habilitar la barra de búsqueda; aquí puedes incluir campos por los que deseas buscar
    search_fields = ('code', 'driving_school__name', 'zone')

    # Permitir filtros usando estos campos
    list_filter = ('driving_school', 'zone')

    # Especificar el orden por defecto de los objetos en la lista (opcional)
    ordering = ('driving_school', 'code')

    # Configurar campos que pueden editarse directamente en la lista (opcional)
    list_editable = ('zone',)

    # Personalizar la forma en que se editan/crean las secciones de autoescuelas
    fieldsets = (
        (None, {
            'fields': ('driving_school', 'code', 'zone')
        }),
    )

