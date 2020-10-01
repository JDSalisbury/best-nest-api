
from .logger import pretty_request
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
import json


class BoxViewSet(viewsets.ModelViewSet):

    serializer_class = BoxSerializer
    queryset = Box.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        id = self.request.query_params.get('box')

        if id:
            return Task.objects.filter(box=id)

        return self.queryset


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def partial_update(self, request, *args, **kwargs):

        print("pUpdate")
        y = json.loads(str(request.data['meta_data']).replace("'", '"'))

        print(y['heating_up'])

        print(*args)
        return super().partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('updated')
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print(super().list(request, *args, **kwargs).data)
        return super().list(request, *args, **kwargs)
