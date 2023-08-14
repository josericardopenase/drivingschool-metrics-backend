# views.py
from rest_framework import viewsets
from .models import TestCenter, TestType, Test
from .serializers import TestCenterSerializer, TestTypeSerializer, TestSerializer

class TestCenterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TestCenter.objects.all()
    serializer_class = TestCenterSerializer

class TestTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer

class TestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Test.objects.all()
    serializer_class = TestSerializer
