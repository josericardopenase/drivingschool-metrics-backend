from rest_framework.decorators import api_view
from rest_framework.response import Response
from tests.models import Test, TestType
from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from rest_framework import serializers
from django.db.models import Sum
from metrics.filters import *

@api_view()
def graph1(request):

    metrica_param = request.query_params.get('metrica', "num_presentados") 

    # parámetros autoescuelas
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    autoescuelas_obj = DrivingSchool.objects.filter(name__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    filters = [
        #DateFilterField(),
        DrivingSchoolFilterField(),
        #MetricFilterField(), # nº aprobados, nºaptos o nºno aptos
        PermissionFilterField(), 
        ProvinceFilterField(),
        TestCenterFilterField(),
        TestTypeFilterField()]

    query_filter = QueryFilter(filters, request.query_params)
    query_filter.validate_params()
    filter_params = query_filter.combine_filters()
    print(filter_params)
    
    final_result = [None] * 37

    for autoescuela in autoescuelas_obj:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela)
        result = Test.objects.filter(**filter_params).values('month', 'year').annotate(valor=Sum(metrica_param))
        
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