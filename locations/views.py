# views.py
from rest_framework import viewsets
from .models import Province
from .serializers import ProvinceSerializer
from rest_framework.permissions import IsAuthenticated

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = (IsAuthenticated, )
