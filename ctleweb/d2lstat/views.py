from django.shortcuts import render

from .d2lstat import process_file
from .forms import UploadFileForm


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            process_file(request.FILES['usage'].temporary_file_path(),
                         request.FILES['full'].temporary_file_path(),
                         request.FILES['part'].temporary_file_path(),
                         request.POST['semester'],
                         request.POST['total_courses'])
            return render(request, 'd2lstat/report.html')
    else:
        form = UploadFileForm()
    return render(request, 'd2lstat/index.html', {'form': form})