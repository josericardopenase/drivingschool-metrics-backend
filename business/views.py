from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from business.models import Section, DrivingLicense
from business.serializers import SectionSerializer, DrivingLicenseSerializer

# Create your views here.
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

class DrivingLicenseViewSet(viewsets.ModelViewSet):
    queryset = DrivingLicense.objects.all()
    serializer_class = DrivingLicenseSerializer
    permission_classes = [IsAuthenticated]
