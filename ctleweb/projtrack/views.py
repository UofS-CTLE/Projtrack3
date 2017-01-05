from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from .forms import LoginForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("No.")
    else:
        form = LoginForm()
    return render(request, 'projtrack/index.html', {'form': form})

def home(request):
    return HttpResponse("Hello!")

def logout_view(request):
    logout(request)
