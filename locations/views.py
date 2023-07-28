# views.py
from rest_framework import viewsets
from .models import Province
from .serializers import ProvinceSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
