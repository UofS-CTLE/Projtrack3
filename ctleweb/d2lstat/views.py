from django.shortcuts import render

from .d2lstat import process_file, calculateVirtualClassroomStats, facultyNotUsingD2LCalculation
from .forms import UploadFileForm, VirtualClassroomUsageForm, FacultyNotUsingD2LForm


def index(request):
    if request.method == 'POST':
        process_file(request.FILES['usage'].temporary_file_path(),
                     request.FILES['full'].temporary_file_path(),
                     request.FILES['part'].temporary_file_path(),
                     request.POST['semester'],
                     request.POST['total_courses'])
        return render(request, 'd2lstat/report.html')
    else:
        form = UploadFileForm()
    return render(request, 'd2lstat/index.html', {'form': form})

def virtualClassroomStats(request):
    if request.method == 'POST':
        statsList = calculateVirtualClassroomStats(request.FILES['usage'].temporary_file_path(),
                     request.FILES['full'].temporary_file_path(),
                     request.FILES['part'].temporary_file_path(),
                    request.FILES['virtualClassroomData'].temporary_file_path())
        return render(request, 'd2lstat/virtualClassroomStatsResults.html', {'statsList':statsList})
    else:
        form = VirtualClassroomUsageForm()
        return render(request, 'd2lstat/virtualClassroomStats.html', {'form': form})

def facultyNotUsingD2L(request):
    if request.method == 'POST':
        statsList = facultyNotUsingD2LCalculation(request.FILES['usage'].temporary_file_path(),
                     request.FILES['full'].temporary_file_path(),
                     request.FILES['part'].temporary_file_path(),
                     request.POST['semester'])
        return render(request, 'd2lstat/FacultyNotUsingD2LResults.html', {'statsList':statsList})
    else:
        form = FacultyNotUsingD2LForm()
        return render(request, 'd2lstat/FacultyNotUsingD2L.html', {'form': form})
