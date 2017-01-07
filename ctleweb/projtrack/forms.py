from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class AddProjectForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
