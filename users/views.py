from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })


class IsAuthenticatedView(APIView):
    permission_classes = []

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"authenticated": True})
        return Response({"authenticated": False})
