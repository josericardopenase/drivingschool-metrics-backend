from drivingschools.serializers import DrivingSchoolSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=['GET'])
    def driving_school(self, request):
        user = self.get_object()
        driving_school = user.driving_school  # Assuming 'driving_school' is a field in the User model
        return Response({'driving_school': driving_school})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_driving_school(request):
    user = request.user
    serializer = DrivingSchoolSerializer(user.driving_school) # Assuming 'driving_school' is a field in the User model
    return Response(serializer.data)