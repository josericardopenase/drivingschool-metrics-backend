# views.py
from rest_framework import viewsets
from .models import TestCenter, TestType, Test
from .serializers import TestCenterSerializer, TestTypeSerializer, TestSerializer

class TestCenterViewSet(viewsets.ModelViewSet):
    queryset = TestCenter.objects.all()
    serializer_class = TestCenterSerializer

class TestTypeViewSet(viewsets.ModelViewSet):
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
