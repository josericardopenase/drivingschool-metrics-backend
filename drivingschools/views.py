from rest_framework import viewsets
from .models import DrivingPermission, DrivingSchool, DrivingSchoolSection
from .serializers import DrivingSchoolSerializer, DrivingPermissionSerializer, DrivingSchoolSectionSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class DrivingSchoolViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchool.objects.all()
    serializer_class = DrivingSchoolSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['id']

class DrivingPermissionViewSet(viewsets.ModelViewSet):
    queryset = DrivingPermission.objects.all()
    serializer_class = DrivingPermissionSerializer

class DrivingSchoolSectionViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchoolSection.objects.all()
    serializer_class = DrivingSchoolSectionSerializer
