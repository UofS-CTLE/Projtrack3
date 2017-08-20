from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .forms import AddProjectForm, AddClientForm, AddDeptForm, AddTypeForm, GenerateReportForm
from .forms import LoginForm
from .models import Client, Project, Semester
from .report_generator import Report


# noinspection PyUnusedLocal
def issues(request):
    return redirect('https://github.com/cyclerdan/Projtrack3/issues')


# noinspection PyUnusedLocal
def wiki(request):
    return redirect('https://github.com/cyclerdan/Projtrack3/wiki')


def index(request):
    if request.user.is_authenticated():
        return redirect('projtrack:home')
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
                    'start_date': (
                        request.POST['start_date_month'] + "/" +
                        request.POST['start_date_day'] + "/" +
                        request.POST['start_date_year']
                    ),
                    'end_date': (
                        request.POST['end_date_month'] + "/" +
                        request.POST['end_date_day'] + "/" +
                        request.POST['end_date_year']
                    ),
                    'semester': request.POST['semester'],
                    'user': request.POST['user'],
                    'client': request.POST['client'],
                    'department': request.POST['department'],
                    'proj_type': request.POST['proj_type'],
                    'projects_per_user': request.POST.get('projects_per_user', False),
                    'projects_per_dept': request.POST.get('projects_per_dept', False),
                    'projects_per_type': request.POST.get('projects_per_type', False),
                    'stats_and_metrics': request.POST.get('stats_and_metrics', False)
                }
                Report(req)
                return render(request, 'projtrack/report_page.html')
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
            # noinspection PyUnresolvedReferences
            query = Project.objects.filter(semester=Semester.objects.get(pk=settings.SEMESTER)).order_by('-date')
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


def all_projects(request):
    if request.user.is_authenticated:
        # noinspection PyUnresolvedReferences
        try:
            projects = Project.objects.filter(semester=Semester.objects.get(pk=settings.SEMESTER)).order_by('-date')
        except ObjectDoesNotExist:
            projects = ""
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
                error = "Form submitted successfully."
            else:
                error = "Form is invalid."
        else:
            form = AddProjectForm()
        return render(request, 'projtrack/add_project.html',
                      {'user': request.user, 'title_text': "Add Project", 'form': form,
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
                error = "Form submitted successfully."
            else:
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
        # noinspection PyUnresolvedReferences
        clients = Client.objects.all().order_by('last_name')
        return render(request, 'projtrack/list_view.html',
                      {'title_text': "All Clients", 'user': request.user,
                       'list_view': clients})
    else:
        return redirect('projtrack:not_logged_in')


# noinspection PyShadowingBuiltins
def client_projects(request, id=None):
    if request.user.is_authenticated:
        # noinspection PyUnresolvedReferences
        client = Client.objects.get(id=id)
        try:
            # noinspection PyUnresolvedReferences
            projects = list(Project.objects.filter(client=client))
        except TypeError:
            # noinspection PyUnresolvedReferences
            projects = [Project.objects.get(client=client)]
        return render(request, 'projtrack/client_projects.html',
                      {'title_text': "Projects for " + str(client), 'user': request.user,
                       'list_view': projects})
    else:
        return redirect('projtrack:not_logged_in')


# noinspection PyShadowingBuiltins
def edit_project(request, id=None):
    error = ""
    if request.user.is_authenticated:
        if request.method == 'POST':
            # noinspection PyUnresolvedReferences
            form = AddProjectForm(request.POST or None, instance=Project.objects.get(id=id))
            if form.is_valid():
                t = form.save()
                t.save()
                form = AddProjectForm()
                error = "Form submitted successfully."
            else:
                error = "Form is invalid."
        else:
            project = get_object_or_404(Project, pk=id)
            form = AddProjectForm(instance=project)
        return render(request, 'projtrack/project_edit.html',
                      {'user': request.user, 'title_text': "Edit Project", 'form': form, 'error_message': error,
                       'id': id})
    else:
        return redirect('projtrack:not_logged_in')


# noinspection PyShadowingBuiltins
def project_delete(request, id=None):
    if request.user.is_authenticated:
        try:
            p = get_object_or_404(Project, pk=id)
            projects = []
            u = User.objects.get(username=request.user.username)
            # noinspection PyUnresolvedReferences
            Project.objects.filter(id=p.id).delete()
            # noinspection PyUnresolvedReferences
            query = Project.objects.all().order_by('title')
            for x in query:
                if x.users.username == u.username:
                    projects.append(x)
        except ObjectDoesNotExist:
            projects = ""
        return render(request, 'projtrack/my_projects.html',
                      {'user': request.user, 'title_text': 'My Projects', 'projects': projects})
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


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'projtrack/change_password.html',
                      {'user': request.user, 'form': form})
    else:
        return redirect('projtrack:not_logged_in')
