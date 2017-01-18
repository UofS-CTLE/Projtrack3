from django.contrib import admin

from .models import User, Client, Project, Department, Type

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Type)
