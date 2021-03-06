from django import forms


class UploadFileForm(forms.Form):
    instructor_usage = forms.FileField()
    full = forms.FileField()
    part = forms.FileField()
    semester = forms.CharField(max_length=50)
    total_courses = forms.CharField(max_length=50)


class VirtualClassroomUsageForm(forms.Form):
    instructor_usage = forms.FileField()
    full = forms.FileField()
    part = forms.FileField()
    virtualClassroomData = forms.FileField()

class FacultyNotUsingD2LForm(forms.Form):
    instructor_usage = forms.FileField()
    full = forms.FileField()
    part = forms.FileField()
    semester = forms.CharField(max_length=50)