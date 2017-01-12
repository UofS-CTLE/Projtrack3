from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import AddProjectForm, AddClientForm, AddDeptForm, AddTypeForm
from .forms import LoginForm
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
        projects = []
        query = Project.objects.all()
        for x in query:
            if x.user.username is request.user.username:
                projects.append(x)
        return render(request, 'projtrack/my_projects.html',
                      {'title_text': 'My Projects',
                       'projects': projects})
    else:
        return HttpResponseRedirect('/not_logged_in/')


def all_projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.all()
        return render(request, 'projtrack/list_view.html',
                      {'title_text': "All Projects",
                       'list_view': projects})
    else:
        return HttpResponseRedirect('/not_logged_in/')


def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddProjectForm(request.POST)
            if form.is_valid():
                # Project is added to the database here.
                t = form.save()
                t.save()
        else:
            form = AddProjectForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Project", 'form': form,
                       'form_page': "/add_project/"})
    else:
        return HttpResponseRedirect('/not_logged_in/')


def add_client(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddClientForm(request.POST)
            if form.is_valid():
                t = form.save()
                t.save()
        else:
            form = AddClientForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Client", 'form': form,
                       'form_page': "/add_client/"})
    else:
        return HttpResponseRedirect('/not_logged_in/')


def client_view(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        return render(request, 'projtrack/list_view.html',
                      {'title_text': "All Clients",
                       'list_view': clients})
    else:
        return HttpResponseRedirect('/not_logged_in')


def add_department(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddDeptForm(request.POST)
            if form.is_valid():
                d = form.save()
                d.save()
                form = AddDeptForm()
            form = AddDeptForm()
        else:
            form = AddDeptForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Department", 'form': form,
                       'form_page': "/add_department/"})
    else:
        return HttpResponseRedirect('/not_logged_in/')


def add_type(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddTypeForm(request.POST)
            if form.is_valid():
                t = form.save()
                t.save()
        else:
            form = AddTypeForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Type", 'form': form,
                       'form_page': "/add_type/"})

    else:
        return HttpResponseRedirect('/not_logged_in/')


def not_logged_in(request):
    return render(request, 'projtrack/not_logged_in.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
