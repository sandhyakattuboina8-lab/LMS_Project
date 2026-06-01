from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, UserSerializer


# REGISTER API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# PROFILE API (LOGIN REQUIRED)
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user