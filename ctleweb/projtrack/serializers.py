from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Client, Department, Type


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class ClientSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=False)

    def create(self, validated_data):
        Client.objects.create(**validated_data)

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'department')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer(many=False, read_only=False)
    client = ClientSerializer(many=False, read_only=False)
    users = UserSerializer(many=True, read_only=False)
    type = TypeSerializer(many=False, read_only=False)

    def create(self, validated_data):
        Project.objects.create(**validated_data)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'date', 'type', 'walk_in',
                  'client', 'users', 'semester', 'hours', 'completed')
        extra_kwargs = {'users': {'required': False}, 'description': {'required': False},
                        'title': {'required': False}, 'semester': {'required': False},
                        'client': {'required': False}, 'type': {'required': False}}
