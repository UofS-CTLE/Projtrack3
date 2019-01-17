import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .d2lstat import process_file
from .forms import UploadFileForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            usage = csv.reader(request.FILES['usage'], delimiter='|')
            full = csv.reader(request.FILES['full'], delimiter='|')
            part = csv.reader(request.FILES['part'], delimiter='|')
            process_file(usage,
                         full,
                         part,
                         request.POST['semester'],
                         request.POST['total_courses'])
            return HttpResponseRedirect('')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
