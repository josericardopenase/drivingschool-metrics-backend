from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tests.models import Test, TestType
from drivingschools.models import DrivingSchool, DrivingSchoolSection, DrivingPermission
from rest_framework import serializers
from django.db.models import Sum
from metrics.filters import *
from rest_framework.permissions import IsAuthenticated
import pandas as pd

from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pandas as pd

@api_view()
@permission_classes([IsAuthenticated])
def graph1(request):
    metrica_param = request.query_params.get('metrica', "num_presentados")
    year = request.query_params.get('year', "2023")

    # Parameters for driving schools
    autoescuela_param = request.query_params.get('autoescuela', "")
    autoescuelas = autoescuela_param.split(',') if autoescuela_param else []
    autoescuelas_obj = DrivingSchool.objects.filter(id__in=autoescuelas) if len(autoescuelas) > 0 else DrivingSchool.objects.all()

    # Parameters for permissions
    permiso_param = request.query_params.get('permission', None)
    permisos_obj = DrivingPermission.objects.filter(id__in=permiso_param.split(',')) if permiso_param else DrivingPermission.objects.all()
    
    # Parameters for test types
    tests_params = request.query_params.get('test_type', None)
    tests_obj = TestType.objects.filter(id__in=tests_params.split(',')) if tests_params else TestType.objects.all()

    # Querying the tests
    tests = Test.objects.filter(
        school_section__driving_school__in=autoescuelas_obj, 
        year=year, 
        permission_type__in=permisos_obj, 
        test_type__in=tests_obj
    ).values('month', 'school_section__driving_school__name').annotate(valor=Sum(metrica_param))

    # Convert the query results to a pandas DataFrame
    df = pd.DataFrame(list(tests))

    # Ensure ordering and grouping
    df.sort_values(by=['month'], inplace=True)
    
    # Pivot the DataFrame to have driving schools as columns, months as rows
    pivot_df = df.pivot_table(index='month', columns='school_section__driving_school__name', values='valor', fill_value=0).reset_index()

    # Convert the pivoted DataFrame back to a dictionary format for the response
    final_result = pivot_df.to_dict("records")
    y_labels = pivot_df.columns.tolist()
    y_labels.remove('month')  # Remove the month column from the labels

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

    autoescuela_param = request.query_params.get('autoescuela', "1")
    autoescuela_obj = DrivingSchool.objects.get(id=autoescuela_param)

    permiso_param = request.query_params.get('permission', None)
    permisos_obj = DrivingPermission.objects.filter(id__in=permiso_param.split(',')) if permiso_param else DrivingPermission.objects.all()

    tests_params = request.query_params.get('test_type', None)
    tests_obj = TestType.objects.filter(id__in=tests_params.split(',')) if tests_params else TestType.objects.all()

    df_list = []

    for year in years:
        sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela_obj)
        tests = Test.objects.filter(
            school_section__in=sections, 
            year=year, 
            permission_type__in=permisos_obj, 
            test_type__in=tests_obj
        ).values('month', 'year').annotate(valor=Sum(metrica_param))

        # Convert each year's data into a DataFrame and append to df_list
        if tests:
            df_year = pd.DataFrame(list(tests))
            df_year['label'] = f"{autoescuela_obj.name} {year}"
            df_list.append(df_year)

    if df_list:
        # Concatenate all DataFrames into a single DataFrame
        df = pd.concat(df_list, ignore_index=True)

        # Pivot the DataFrame to have years as columns, months as rows
        pivot_df = df.pivot_table(index='month', columns='label', values='valor', fill_value=0).reset_index()

        # Ensure the month column is sorted numerically
        pivot_df['month'] = pd.to_numeric(pivot_df['month'])
        pivot_df.sort_values('month', inplace=True)

        # Convert the pivoted DataFrame back to a dictionary format for the response
        final_result = pivot_df.to_dict("records")
        y_labels = pivot_df.columns.tolist()
        y_labels.remove('month')
    else:
        final_result = []
        y_labels = []

    return Response({
        "info": {
            "x_label": "month",
            "y_labels": y_labels
        },
        "records": final_result
    })