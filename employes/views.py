from django.shortcuts import render
from .models import Employe
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeSerializer

# Create your views here.
class EmployeList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class EmployeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
