from django import forms
from django.forms import ModelForm

from .models import Type, Client, User, Department, Project


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        field = '__all__'
        exclude = ()

class AddClientForm(ModelForm):
    class Meta:
        model = Client
        field = '__all__'
        exclude = ()

class AddDeptForm(ModelForm):
    class Meta:
        model = Department
        field = '__all__'
        exclude = ()

class AddTypeForm(ModelForm):
    class Meta:
        model = Type
        field = '__all__'
        exclude = ()
