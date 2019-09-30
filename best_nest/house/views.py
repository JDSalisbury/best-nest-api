from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets


class HouseViewSet(viewsets.ModelViewSet):

    serializer_class = HouseSerializer
    queryset = House.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
