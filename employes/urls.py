from django.urls import path
from .views import EmployeList, EmployeDetail

urlpatterns = [
    path('', EmployeList.as_view()),
    path('<str:pk>', EmployeDetail.as_view()),
]
