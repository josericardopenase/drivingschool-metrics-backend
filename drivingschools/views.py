from rest_framework import viewsets
from .models import DrivingPermission, DrivingSchool, DrivingSchoolSection
from .serializers import DrivingSchoolSerializer, DrivingPermissionSerializer, DrivingSchoolSectionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class DrivingSchoolViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchool.objects.all()
    serializer_class = DrivingSchoolSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['id']
    permission_classes = (IsAuthenticated, )

class DrivingPermissionViewSet(viewsets.ModelViewSet):
    queryset = DrivingPermission.objects.all()
    serializer_class = DrivingPermissionSerializer
    permission_classes = (IsAuthenticated, )

class DrivingSchoolSectionViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchoolSection.objects.all()
    serializer_class = DrivingSchoolSectionSerializer
    permission_classes = (IsAuthenticated, )
