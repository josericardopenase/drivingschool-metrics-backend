# views.py
from rest_framework import viewsets
from .models import TestCenter, TestType, Test
from .serializers import TestCenterSerializer, TestTypeSerializer, TestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class TestCenterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TestCenter.objects.all()
    serializer_class = TestCenterSerializer

class TestTypeViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['id']
    permission_classes = (IsAuthenticated, )
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer

class TestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Test.objects.all()
    serializer_class = TestSerializer
