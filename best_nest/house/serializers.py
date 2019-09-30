from .models import *
from rest_framework import serializers


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
