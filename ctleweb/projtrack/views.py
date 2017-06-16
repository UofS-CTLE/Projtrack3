from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets

from .forms import AddProjectForm, AddClientForm, AddDeptForm, AddTypeForm, GenerateReportForm
from .forms import LoginForm
from .models import Client, Project, User, Type
from .report_generator import generate_report
from .serializers import ProjectSerializer, TypeSerializer, DepartmentSerializer, ClientSerializer


def issues(request):
    return redirect('https://github.com/cyclerdan/Projtrack3/issues')


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('projtrack:home')
            else:
                return render(request,
                              'projtrack/index.html',
                              {'user': request.user, 'error_message': "Invalid username or password.",
                               'form': form})
    else:
        form = LoginForm()
        return render(request, 'projtrack/index.html', {'form': form, 'user': request.user})


def home(request):
    if request.user.is_authenticated:
        return render(request, 'projtrack/home.html', {'user': request.user})
    else:
        return redirect('projtrack:not_logged_in')


def report_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = GenerateReportForm(request.POST)
            if form.is_valid():
                req = {
                    'start_date': request.POST['start_date'],
                    'end_date': request.POST['end_date'],
                    'semester': request.POST['semester'],
                    'user': request.POST['user'],
                    'client': request.POST['client'],
                    'department': request.POST['department'],
                    'proj_type': request.POST['proj_type'],
                    'sort_by_date': request.POST.get('sort_by_date')
                }
                report = generate_report(req)
                return render(request, 'projtrack/report_page.html',
                              {'user': request.user, 'report': report})
        else:
            form = GenerateReportForm()
            return render(request,
                          'projtrack/report_generator.html',
                          {'user': request.user, 'title_text': 'Generate a Report',
                           'form': form})
    else:
        return redirect('projtrack:not_logged_in')


def my_projects(request):
    if request.user.is_authenticated:
        try:
            projects = []
            u = User.objects.get(username=request.user.username)
            query = Project.objects.all()
            for x in query:
                if x.users.username == u.username and not x.deleted:
                    projects.append(x)
        except ObjectDoesNotExist:
            projects = ""
        return render(request, 'projtrack/my_projects.html',
                      {'user': request.user, 'title_text': 'My Projects',
                       'projects': projects})
    else:
        return redirect('projtrack:not_logged_in')


def all_projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.all()
        return render(request, 'projtrack/all_projects.html',
                      {'user': request.user, 'title_text': "All Projects",
                       'list_view': projects})
    else:
        return redirect('projtrack:not_logged_in')


def add_project(request):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddProjectForm(request.POST)
            if form.is_valid():
                # Project is added to the database here.
                t = form.save()
                t.save()
                form = AddProjectForm()
            else:
                error = "Form is invalid."
        else:
            form = AddProjectForm()
        return render(request, 'projtrack/add_project.html',
                      {'user': request.user, 'title_text': "Add Project", 'form': form,
                       'error_message': error})
    else:
        return redirect('projtrack:not_logged_in')


def edit_project(request, id):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            project = Project.objects.get(id=id)
            form = AddProjectForm(request.POST or None, instance=project)
            if form.is_valid():
                t = form.save()
                t.save()
                form = AddProjectForm()
            else:
                error = "Form is invalid."
        else:
            project = Project.objects.get(id=id)
            form = AddProjectForm(instance=project)
        return render(request, 'projtrack/project_edit.html',
                      {'user': request.user, 'title_text': "Edit Project", 'form': form,
                       'error_message': error})
    else:
        return redirect('projtrack:not_logged_in')


def add_client(request):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddClientForm(request.POST)
            if form.is_valid():
                t = form.save()
                t.save()
                form = AddClientForm()
                error = "Form is invalid."
        else:
            form = AddClientForm()
        return render(request, 'projtrack/add_client.html',
                      {'user': request.user, 'title_text': "Add Client", 'form': form,
                       'error_message': error})
    else:
        return redirect('projtrack:not_logged_in')


def client_view(request):
    if request.user.is_authenticated:
        clients = Client.objects.all()
        return render(request, 'projtrack/list_view.html',
                      {'title_text': "All Clients", 'user': request.user,
                       'list_view': clients})
    else:
        return redirect('projtrack:not_logged_in')


def project_delete(request, id=None):
    if request.user.is_authenticated:
        try:
            p = get_object_or_404(Project, pk=id)
            projects = []
            u = User.objects.get(username=request.user.username)
            Project.objects.filter(id=p.id).delete()
            query = Project.objects.all()
            for x in query:
                if x.users.username == u.username:
                    projects.append(x)
        except ObjectDoesNotExist:
            projects = ""
        return render(request, 'projtrack/my_projects.html',
                      {'user': request.user, 'title_text': 'My Projects',
                       'projects': projects})
    else:
        return redirect('projtrack:not_logged_in')


def add_department(request):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddDeptForm(request.POST)
            if form.is_valid():
                d = form.save()
                d.save()
                form = AddDeptForm()
                error = "Form submitted successfully."
            else:
                error = "Form is invalid."
        else:
            form = AddDeptForm()
        return render(request, 'projtrack/add_department.html',
                      {'user': request.user, 'title_text': "Add Department", 'form': form,
                       'error_message': error})
    else:
        return redirect('projtrack:not_logged_in')


def add_type(request):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddTypeForm(request.POST)
            if form.is_valid():
                t = form.save()
                t.save()
                form = AddTypeForm()
                error = "Form submitted successfully."
            else:
                error = "Form is invalid."
        else:
            form = AddTypeForm()
        return render(request, 'projtrack/add_type.html',
                      {'user': request.user, 'title_text': "Add Type", 'form': form,
                       'error_message': error})
    else:
        return redirect('projtrack:not_logged_in')


def not_logged_in(request):
    return render(request, 'projtrack/not_logged_in.html')


def logout_view(request):
    logout(request)
    return redirect('projtrack:index')


class ProjectSerializerView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ClientSerializerView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DepartmentSerializerView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = DepartmentSerializer


class TypeSerializerView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

