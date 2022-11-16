
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

# Create your views here.
class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
