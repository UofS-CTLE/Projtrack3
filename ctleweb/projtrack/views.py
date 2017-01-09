from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from .forms import LoginForm
from .forms import AddProjectForm, AddClientForm, AddDeptForm, AddTypeForm
from .models import Client, Project, Type, Department

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return render(request,
                              'projtrack/index.html',
                              {'error_message': "Invalid username or password.",
                               'form': form})
    else:
        form = LoginForm()
        return render(request, 'projtrack/index.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'projtrack/home.html')
    else:
        return HttpResponseRedirect('/not_logged_in/')

def my_projects(request):
    if request.user.is_authenticated:
        return render(request, 'projtrack/my_projects.html')
    else:
        return HttpResponseRedirect('/not_logged_in/')

def all_projects(request):
    if request.user.is_authenticated:
        return render(request, 'projtrack/all_projects.html')
    else:
        return HttpResponseRedirect('/not_logged_in/')

def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddProjectForm(request.POST)
            if form.is_valid():
                # Project is added to the database here.
                t = Project()
                t.title = request.POST['title']
                t.description = request.POST['description']
                t.type = request.POST['type']
                t.walk_in = request.POST['walk_in']
                t.client = request.POST['client']
                t.users = request.POST['users']
                t.save()
        else:
            form = AddProjectForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Project", 'form': form})
    else:
        return HttpResponseRedirect('/not_logged_in/')

def add_client(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddClientForm(request.POST)
            if form.is_valid():
                t = Client()
                t.first_name['first_name']
                t.last_name['last_name']
                t.email = request.POST['email']
                t.save()
        else:
            form = AddClientForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Client", 'form': form})
    else:
        return HttpResponseRedirect('/not_logged_in/')

def add_department(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddDeptForm(request.POST)
            if form.is_valid():
                t = Department()
                t.name = request.POST['name']
                t.save()
        else:
            form = AddDeptForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Department", 'form': form})
    else:
        return HttpResponseRedirect('/not_logged_in/')

def add_type(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddTypeForm(request.POST)
            if form.is_valid():
                t = Type()
                t.name = request.POST['name']
                t.save()
        else:
            form = AddTypeForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Type", 'form': form})

    else:
        return HttpResponseRedirect('/not_logged_in/')

def not_logged_in(request):
    return render(request, 'projtrack/not_logged_in.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
