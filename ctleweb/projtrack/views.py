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
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm()
    return render(request, 'projtrack/index.html', {'form': form})

def logout_view(request):
    logout(request)
