from rest_framework.decorators import api_view
from rest_framework.response import Response
from tests.models import Test
from drivingschools.models import DrivingSchool, DrivingSchoolSection
from rest_framework import serializers
from django.db.models import Sum

@api_view()
def graph1(request):
    print(request.query_params.get('autoescuela').split(','))
    
    #year = request.query_params['year']
    autoescuela = DrivingSchool.objects.get(name='AUTOESCUELA ECO')
    sections = DrivingSchoolSection.objects.filter(driving_school=autoescuela)
    result = Test.objects.filter(year=2022, school_section__in=sections).values('month', 'year').annotate(num_presentados=Sum('num_presentados'))

    lista = [x for x in result]

    return Response(lista)