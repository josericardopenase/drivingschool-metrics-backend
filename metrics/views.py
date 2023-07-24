from rest_framework.decorators import api_view
from rest_framework.response import Response
from tests.models import Test
from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from rest_framework import serializers
from django.db.models import Sum

@api_view()
def graph1(request):

    # parámetros autoescuelas
    metrica_param = request.query_params.get('metrica', "num_presentados") 
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas) if len(autoescuelas) == 0 else DrivingSchool.objects.all()

    # parámetros permisos
    permiso_param = request.query_params.get('permiso')
    permisos = permiso_param.split(',') if permiso_param else []
    print(permisos)
    permisos_obj = DrivingPermission.objects.filter(name__in=permisos)
    print(permisos_obj)



    year = request.query_params.get('year')

    final_result =  [None] * 12

    for autoescuela in autoescuelas_obj:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela)
        result = Test.objects.filter(year=year, school_section__in=sections, permission_type__in=permisos_obj).values('month', 'year').annotate(valor=Sum(metrica_param))
        
        for row in range(0, len(result)):
            if final_result[row] == None:
                final_result[row] = {
                    "month": result[row]["month"],
                    "year": result[row]["year"],
                    autoescuela.name : result[row]["valor"]

                }
            else:
                final_result[row] = {
                    **final_result[row],
                    autoescuela.name : result[row]["valor"]
                }
    
    final_result = [x for x in final_result if x is not None]

    return Response(final_result)
