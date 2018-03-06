import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Client, Department, Type, Semester, CurrentSemester


class DepartmentSerializer(serializers.ModelSerializer):
    queryset = Department.objects.all()

    class Meta:
        model = Department
        fields = ('id', 'name')


class ClientSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    queryset = Client.objects.all()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'department')


class TypeSerializer(serializers.ModelSerializer):
    queryset = Type.objects.all()

    class Meta:
        model = Type
        fields = ('id', 'name')


class SemesterSerializer(serializers.ModelSerializer):
    queryset = Semester.objects.all()

    class Meta:
        model = Semester
        fields = ('id', 'name')


class CurrentSemesterSerializer(serializers.ModelSerializer):
    queryset = CurrentSemester.objects.all()

    class Meta:
        model = CurrentSemester
        fields = ('id', 'semester')


class UserSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    queryset = Project.objects.filter(semester=CurrentSemester.objects.all()[0].semester)
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    users = UserSerializer(many=True, read_only=False)
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())

    def create(self, validated_data):
        return Project.objects.create(
            title=validated_data.get("title", None),
            description=validated_data.get("description", None),
            date=str(datetime.date.today()),
            type=validated_data.get("type"),
            walk_in=validated_data.get("walk_in", None),
            client=validated_data.get("client"),
            semester=validated_data.get("semester"),
            hours=validated_data.get("hours", None),
            completed=validated_data.get("completed", None)
        )

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'date', 'type', 'walk_in',
                  'client', 'users', 'semester', 'hours', 'completed')
        extra_kwargs = {'users': {'required': False}, 'description': {'required': False},
                        'title': {'required': False}, 'semester': {'required': False},
                        'client': {'required': False}, 'type': {'required': False}}
