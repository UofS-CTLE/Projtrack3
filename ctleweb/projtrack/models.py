import datetime

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


def get_name(self):
    return str(self.first_name) + " " + str(self.last_name)


User.add_to_class('__str__', get_name)


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = u'Department'
        ordering = ['name']

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE)

    class Meta:
        db_table = u'Client'
        ordering = ['last_name']

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)


class Type(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = u'Type'
        ordering = ['name']

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = u'Semester'
        ordering = ['name']

    def __str__(self):
        return self.name


class CurrentSemester(models.Model):
    semester = models.ForeignKey(Semester)

    class Meta:
        db_table = u'CurrentSemester'

    def __str__(self):
        return str(self.semester)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(editable=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    walk_in = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    users = models.ManyToManyField(User)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, blank=True, null=True)
    hours = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = u'Project'
        ordering = ['date']

    def __str__(self):
        return self.title
