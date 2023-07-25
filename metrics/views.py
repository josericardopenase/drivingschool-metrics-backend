from rest_framework.decorators import api_view
from rest_framework.response import Response
from tests.models import Test, TestType
from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from rest_framework import serializers
from django.db.models import Sum
from filters.models import QueryFilter

@api_view()
def graph1(request):

    metrica_param = request.query_params.get('metrica', "num_presentados") 

    # parámetros autoescuelas
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    # parámetros permisos
    permiso_param = request.query_params.get('permiso', "")
    permisos = permiso_param.split(',') if permiso_param else []
    permisos_obj = DrivingPermission.objects.filter(name__in=permisos) if len(permisos) > 0 else DrivingPermission.objects.all()

    # será el número de meses from & to 
    year = request.query_params.get('year')
    
    final_result = [None] * 12



    filters = QueryFilter([ProvinceFilterField(), DrivingSchoolFilterField], request.query_params)
    Test.objecs.filter(**filters.filter())

    for autoescuela in autoescuelas_obj:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela)

        params = {
            'year': year,
            'school_section__in': sections,
            'permission_type__in': permisos_obj,
        }

        result = Test.objects.filter(params).values('month', 'year').annotate(valor=Sum(metrica_param))
        
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

@api_view()
def graph2(request):

    # parámetros autoescuelas
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    print(len(autoescuelas))
    autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    # parámetros permisos
    permiso_param = request.query_params.get('permiso')
    permisos = permiso_param.split(',') if permiso_param else []
    print(permisos)
    permisos_obj = DrivingPermission.objects.filter(name__in=permisos) if len(permisos) > 0 else DrivingPermission.objects.all()
    print(permisos_obj)

    # parámetros tipo de examen
    tipo_examen_param = request.query_params.get('tipo_examen')
    tipo_examen = tipo_examen_param.split(',') if tipo_examen_param else []
    print(tipo_examen)
    tipo_examen_obj = TestType.objects.filter(name__in=tipo_examen) if len(tipo_examen) > 0 else TestType.objects.all()
    print(tipo_examen_obj)

    # será el número de meses from & to 

    # Parámetros de rango de fechas
    year= request.query_params.get('year')  
    month= request.query_params.get('month')  
    final_result =  []

    for permiso in permisos_obj:
        sections = DrivingSchoolSection.objects.filter(driving_school__in=autoescuelas_obj)
        result = Test.objects.filter(year=year,
            #month=month,
            test_type__in=tipo_examen_obj,
            school_section__in=sections, 
            permission_type=permiso
        ).values('permission_type').annotate(
        num_presentados=Sum('num_presentados'),
        num_aptos=Sum('num_aptos'))

        print(result)
        
        for row in result:
            final_result.append({
                "num_presentados": row["num_presentados"],
                "num_aptos": row["num_aptos"],
                "num_no_aptos": row["num_presentados"] - row["num_aptos"],
                "permiso" : row["permission_type"]
            })
    
    return Response(final_result)

@api_view()
def graph3(request):

    # parámetros autoescuelas
    autoescuela_param = request.query_params.get('autoescuela', '')
    print(list(autoescuela_param))
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    print(len(autoescuelas))
    autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    # parámetro permiso
    permiso= request.query_params.get('permiso')  

    # será el número de meses from & to 

    # Parámetros de rango de fechas
    year= request.query_params.get('year')  
    month= request.query_params.get('month')  

    print(request.query_params, " hola")

    final_result =  []

    for tipo_examen in TestType.objects.all():
        sections = DrivingSchoolSection.objects.filter(driving_school__in=autoescuelas_obj)
        result = Test.objects.filter(year=year,
            #month=month,
            school_section__in=sections, 
            permission_type=permiso,
            test_type=tipo_examen
        ).values('test_type').annotate(
        num_presentados=Sum('num_presentados'),
        num_aptos=Sum('num_aptos'))

        
        for row in result:
            final_result.append({
                "num_presentados": row["num_presentados"],
                "num_aptos": row["num_aptos"],
                "num_no_aptos": row["num_presentados"] - row["num_aptos"],
                "tipo examen" : row["test_type"]
            })
    
    return Response(final_result)