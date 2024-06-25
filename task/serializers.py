from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"