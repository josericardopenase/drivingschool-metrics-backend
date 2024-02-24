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
    metrica_param = request.query_params.get('metrica', "num_presentados")
    year_param = request.query_params.get('year', "2023")
    section_param = request.query_params.get('section', "")
    sections = section_param.split(',') if section_param else []

    permiso_param = request.query_params.get('permission', "")
    permisos = permiso_param.split(',') if permiso_param else []

    test_type_param = request.query_params.get('test_type', "")
    test_types = test_type_param.split(',') if test_type_param else []

    # Filtrar por secciones específicas, si se proporcionan
    sections_obj = DrivingSchoolSection.objects.filter(id__in=sections) if sections else DrivingSchoolSection.objects.all()

    # Filtrar por permisos específicos, si se proporcionan
    permisos_obj = DrivingPermission.objects.filter(id__in=permisos) if permisos else DrivingPermission.objects.all()

    # Filtrar por tipos de examen específicos, si se proporcionan
    test_types_obj = TestType.objects.filter(id__in=test_types) if test_types else TestType.objects.all()

    df_list = []

    for section in sections_obj:
        tests = Test.objects.filter(
            school_section=section, 
            year=year_param,
            permission_type__in=permisos_obj,
            test_type__in=test_types_obj
        ).values('month', 'year', 'school_section__driving_school__name', 'school_section__code').annotate(valor=Sum(metrica_param))

        if tests:
            df_section = pd.DataFrame(list(tests))
            df_section['label'] = f"{section.driving_school.name} - {section.code} {year_param}"
            df_list.append(df_section)

    if df_list:
        df = pd.concat(df_list, ignore_index=True)
        pivot_df = df.pivot_table(index='month', columns='label', values='valor', fill_value=0).reset_index()
        pivot_df.sort_values('month', inplace=True)
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def autoescuelas_con_mas_presentados(request):
    metrica_param = request.query_params.get('metrica', "num_presentados")
    year = request.query_params.get('year', "2024")

    # Realizar la consulta para obtener el total de 'num_presentados' por autoescuela
    schools_totals = Test.objects.filter(year=year)\
        .values('school_section__driving_school__name')\
        .annotate(total_presentados=Sum(metrica_param))\
        .order_by('-total_presentados')

    # Preparar los datos para la respuesta
    data = []
    for item in schools_totals:
        data.append({
            'autoescuela': item['school_section__driving_school__name'],
            'total_presentados': item['total_presentados']
        })

    # Construir la respuesta
    response = {
        'year': year,
        'metrica': metrica_param,
        'records': data
    }

    return Response(response)

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