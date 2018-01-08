from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, SelectDateWidget

from .models import Type, Client, Department, Project, Semester


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddProjectForm(ModelForm):

    client_first_name = forms.CharField(max_length=100, required=False)
    client_last_name = forms.CharField(max_length=100, required=False)
    client_email = forms.CharField(max_length=100, required=False)
    client_department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(AddProjectForm, self).__init__(*args, **kwargs)
        self.fields['client'].required = False
        self.fields['users'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['users'].queryset = User.objects.filter(is_active=True)

    class Meta:
        model = Project
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        field = '__all__'
        exclude = ('date', 'semester')


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


class DateInput(forms.DateInput):
    input_type = 'date'


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
class GenerateReportForm(forms.Form):
    start_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label=("Year", "Month", "Day"),
                                                                         years=range(2010, 2025)))
    end_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label=("Year", "Month", "Day"),
                                                                       years=range(2010, 2025)))
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(),
                                      required=False)
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True),
                                  required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(),
                                    required=False)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        required=False)
    proj_type = forms.ModelChoiceField(queryset=Type.objects.all(),
                                       required=False)
    show_stats = forms.BooleanField(required=False, initial=False)
