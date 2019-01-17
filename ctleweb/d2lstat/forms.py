from django import forms


class UploadFileForm(forms.Form):
    usage = forms.FileField()
    full = forms.FileField()
    part = forms.FileField()
    semester = forms.CharField(max_length=50)
    total_courses = forms.CharField(max_length=50)
