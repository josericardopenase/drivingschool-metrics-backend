from rest_framework import viewsets
from .models import DrivingPermission, DrivingSchool, DrivingSchoolSection
from .serializers import DrivingSchoolSerializer, DrivingPermissionSerializer, DrivingSchoolSectionSerializer

class DrivingSchoolViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchool.objects.all()
    serializer_class = DrivingSchoolSerializer

class DrivingPermissionViewSet(viewsets.ModelViewSet):
    queryset = DrivingPermission.objects.all()
    serializer_class = DrivingPermissionSerializer

class DrivingSchoolSectionViewSet(viewsets.ModelViewSet):
    queryset = DrivingSchoolSection.objects.all()
    serializer_class = DrivingSchoolSectionSerializer
