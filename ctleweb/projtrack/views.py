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
                t = Project()
                t.title = request.POST['title']
                t.description = request.POST['description']
                t.type = request.POST['type']
                t.walk_in = request.POST['walk_in']
                t.client = request.POST['client']
                t.users = request.POST['users']
                t.save()
        else:
            print("Sending get request.")
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
                t.first_name = request.POST['first_name']
                t.last_name = request.POST['last_name']
                t.email = request.POST['email']
                t.department = request.POST['department']
                t.save()
        else:
            form = AddClientForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Client", 'form': form})
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
    print("Adding department.")
    if request.user.is_authenticated:
        print("User authenticated.")
        if request.method == 'POST':
            print("Method was post.")
            form = AddDeptForm(request.POST)
            if form.is_valid():
                print("The form was valid.")
                d = Department()
                d.name = request.POST['name']
                d.save()
        else:
            print("Method was get.")
            form = AddDeptForm()
        return render(request, 'projtrack/form_page.html',
                      {'title_text': "Add Department", 'form': form})
    else:
        print("Not logged in.")
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
