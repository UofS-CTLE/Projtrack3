from django import forms

from .models import Type, Client, User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class AddProjectForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=500)
    type = forms.ModelMultipleChoiceField(label="Type",
                                          queryset=Type.objects.values_list('name', flat=True))
    walk_in = forms.BooleanField(label="Walk-in?")
    client = forms.ModelMultipleChoiceField(label="Client",
                                             queryset=Client.objects.values_list('last_name', flat=True))
    users = forms.ModelMultipleChoiceField(label="Users",
                                           queryset=User.objects.values_list('username', flat=True))
