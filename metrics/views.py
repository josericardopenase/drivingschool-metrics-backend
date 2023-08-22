from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tests.models import Test, TestType
from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from rest_framework import serializers
from django.db.models import Sum
from metrics.filters import *
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
def graph1(request):

    metrica_param = request.query_params.get('metrica', "num_presentados") 
    year = request.query_params.get('year', 2023) 

    # parámetros autoescuelas
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    autoescuelas_obj = DrivingSchool.objects.filter(id__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    # parámetros permisos
    permiso_param = request.query_params.get('permission', None)
    permisos_obj = DrivingPermission.objects.filter(id__in=permiso_param) if permiso_param else DrivingPermission.objects.all()

    final_result = [None] * 37
    y_labels = []

    for autoescuela in autoescuelas_obj:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela)
        result = Test.objects.filter(school_section__in=sections, year=year, permission_type__in=permisos_obj).values('month', 'year').annotate(valor=Sum(metrica_param))
        
        for row in range(0, len(result)):
            if autoescuela.name not in y_labels: y_labels.append(autoescuela.name)
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

    return Response({
        "info": {
            "x_label": "month",
            "y_labels": y_labels
        },
        "records": final_result
    })

@api_view()
@permission_classes([IsAuthenticated])
def graph2(request):

    # parámetros permisos
    permiso_param = request.query_params.get('permiso')
    permisos = permiso_param.split(',') if permiso_param else []
    permisos_obj = DrivingPermission.objects.filter(name__in=permisos) if len(permisos) > 0 else DrivingPermission.objects.all()

    filters = [
        #DateFilterField(),
        DrivingSchoolFilterField(),
        #MetricFilterField(), # nº aprobados, nºaptos o nºno aptos
        ProvinceFilterField(),
        TestCenterFilterField(),
        TestTypeFilterField()]

    query_filter = QueryFilter(filters, request.query_params)
    query_filter.validate_params()
    filter_params = query_filter.combine_filters()
    print(filter_params)

    final_result =  []

    for permiso in permisos_obj:
        filter_params['permission_type'] = permiso
        result = Test.objects.filter(**filter_params).values('permission_type').annotate(
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
@permission_classes([IsAuthenticated])
def graph3(request):

    filters = [
        #DateFilterField(),
        DrivingSchoolFilterField(),
        #MetricFilterField(), # nº aprobados, nºaptos o nºno aptos
        PermissionFilterField(), 
        ProvinceFilterField(),
        TestCenterFilterField()]

    query_filter = QueryFilter(filters, request.query_params)
    query_filter.validate_params()
    filter_params = query_filter.combine_filters()
    print(filter_params)

    final_result =  []

    for tipo_examen in TestType.objects.all():
        filter_params['test_type'] = tipo_examen
        result = Test.objects.filter(**filter_params).values('test_type').annotate(
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

@api_view()
@permission_classes([IsAuthenticated])
def graph4(request):

    metrica_param = request.query_params.get('metrica', "num_presentados") 
    years_param = request.query_params.get('years', "2023") 
    years = years_param.split(',') if years_param else []

    autoescuela_param = request.query_params.get('autoescuela', 1)
    autoescuelas_obj = DrivingSchool.objects.get(id=autoescuela_param)

    # parámetros permisos
    permiso_param = request.query_params.get('permission', None)
    permisos_obj = DrivingPermission.objects.filter(id__in=permiso_param) if permiso_param else DrivingPermission.objects.all()

    final_result = [None] * 37
    y_labels = []

    print(years)

    for year in years:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuelas_obj)
        result = Test.objects.filter(school_section__in=sections, year=year, permission_type__in=permisos_obj).values('month', 'year').annotate(valor=Sum(metrica_param))
        print("hello")

        for row in range(0, len(result)):
            if autoescuelas_obj.name  + " " + str(year) not in y_labels: y_labels.append(autoescuelas_obj.name  + " " + str(year))
            if final_result[row] == None:
                final_result[row] = {
                    "month": result[row]["month"],
                    "year": result[row]["year"],
                    autoescuelas_obj.name  + " " + str(year) : result[row]["valor"] 
                }
            else:
                final_result[row] = {
                    **final_result[row],
                    autoescuelas_obj.name + " " + str(year) : result[row]["valor"] 
                }
    
    final_result = [x for x in final_result if x is not None]

    return Response({
        "info": {
            "x_label": "month",
            "y_labels": y_labels
        },
        "records": final_result
    })
