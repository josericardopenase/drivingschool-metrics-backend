from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
