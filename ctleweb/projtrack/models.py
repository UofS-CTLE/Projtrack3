from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.email

class User(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    walk_in = models.BooleanField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
