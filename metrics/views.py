from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DgtTests

@api_view()
def graph1(request):


    test1 = DgtTests.objects.first()

    return Response({
        "name": test1.name,
        "aprobados": test1.aprobados,
        "suspensos": test1.presentados - test1.aprobados
    })