import datetime
from collections import OrderedDict

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Project, Client, Department, Type, Semester, CurrentSemester


class DepartmentSerializer(serializers.PrimaryKeyRelatedField):
    queryset = Department.objects.all()

    def to_representation(self, value):
        pk = super(DepartmentSerializer, self).to_representation(value)
        try:
            item = Client.objects.get(pk=pk)
            serializer = DepartmentSerializer(item)
            return serializer.data
        except Client.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])

    class Meta:
        model = Department
        fields = ('id', 'name')


class ClientSerializerProject(serializers.PrimaryKeyRelatedField):
    queryset = Client.objects.all()

    def to_representation(self, value):
        pk = super(ClientSerializerProject, self).to_representation(value)
        try:
            item = Project.objects.get(pk=pk)
            serializer = ClientSerializerProject(item)
            return serializer.data
        except Project.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'department')


class ClientSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=False)
    queryset = Client.objects.all()

    def create(self, validated_data):
        Client.objects.create(**validated_data)

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'department')


class TypeSerializer(serializers.PrimaryKeyRelatedField):
    queryset = Type.objects.all()

    def to_representation(self, value):
        pk = super(TypeSerializer, self).to_representation(value)
        try:
            item = Project.objects.get(pk=pk)
            serializer = TypeSerializer(item)
            return serializer.data
        except Project.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])

    class Meta:
        model = Type
        fields = ('id', 'name')


class SemesterSerializer(serializers.PrimaryKeyRelatedField):
    queryset = Semester.objects.all()

    def to_representation(self, value):
        pk = super(SemesterSerializer, self).to_representation(value)
        try:
            item = Project.objects.get(pk=pk)
            serializer = SemesterSerializer(item)
            return serializer.data
        except Project.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])

    class Meta:
        model = Type
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    queryset = Project.objects.filter(semester=CurrentSemester.objects.all()[0].semester)
    semester = SemesterSerializer(many=False, read_only=False)
    client = ClientSerializerProject(many=False, read_only=False)
    users = UserSerializer(many=True, read_only=False)
    type = TypeSerializer(many=False, read_only=False)

    def create(self, validated_data):
        Project.objects.create(
            title=validated_data.get("title", None),
            description=validated_data.get("description", None),
            date=str(datetime.date.today()),
            type=Type.objects.get(pk=self.kwargs['type_id']),
            walk_in=validated_data.get("walk_in", None),
            client=Client.objects.get(pk=self.kwargs['client_id']),
            users=get_object_or_404(User, self.request.user.username),
            semester=Semester.objects.get(pk=self.kwargs['semester_id']),
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
