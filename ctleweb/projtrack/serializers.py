from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Client, Department, Type


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
