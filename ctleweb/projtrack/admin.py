from django.contrib import admin

from .models import Client, Project, Department, Type, Semester

# Register your models here.

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Type)
admin.site.register(Semester)
