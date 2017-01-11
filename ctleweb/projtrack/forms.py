from django import forms

from .models import Type, Client, User, Department


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddProjectForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=500,
                                  widget=forms.Textarea)
    type = forms.ModelMultipleChoiceField(label="Type",
                                          queryset=Type.objects.values_list('name', flat=True))
    walk_in = forms.BooleanField(label="Walk-in?")
    client = forms.ModelMultipleChoiceField(label="Client",
                                            queryset=Client.objects.values_list('email', flat=True))
    users = forms.ModelMultipleChoiceField(label="Users",
                                           queryset=User.objects.values_list('username', flat=True))


class AddClientForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.CharField(label="Email Address", max_length=100)
    department = forms.ModelMultipleChoiceField(label="Department",
                                                queryset=Department.objects.values_list('name', flat=True))


class AddDeptForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)


class AddTypeForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
