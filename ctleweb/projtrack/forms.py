from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Type, Client, Department, Project, Semester


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        field = '__all__'
        exclude = ('date', 'deleted')


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


class GenerateReportForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(),
                                      required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(),
                                    required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        required=False)
    proj_type = forms.ModelChoiceField(queryset=Type.objects.all(),
                                       required=False)
    sort_by_date = forms.BooleanField(required=False, initial=False)
