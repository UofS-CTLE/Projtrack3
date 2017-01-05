from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)

class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Department(models.Model):
    name = models.CharField(max_length=200)

class Type(models.Model):
    name = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    walk_in = models.NullBooleanField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

