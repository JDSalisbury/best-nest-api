from .models import *
from rest_framework import serializers


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    # Box = BoxSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # Box = serializers.StringRelatedField()
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    def get_meta_data(self, obj):
        return_data = None
        if type(obj.meta_data) == list:
            embedded_list = []
            for item in obj.meta_data:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.meta_data.__dict__
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data
