from datetime import datetime

from .models import Project, Semester

def check_dates(s_d, e_d):
    if s_d != '':
        s_d = datetime.strptime(s_d, "%Y-%m-%d")
    if e_d != '':
        e_d = datetime.strptime(e_d, "%Y-%m-%d")
    result = list(Project.objects.all())
    for x in result:
        if x.date > e_d:
            result.remove(x)
        if x.date < s_d:
            result.remove(x)
    return result

def check_semester(semester):
    if semester != '':
        sem = Semester.objects.get(name=str(semester))
        return list(Project.objects.get(semester=sem))
    else:
        return list(Project.objects.all())

def check_user(user):
    use = User.objects.get(name=str(user))
    return list(Project.objects.get(users=use))

def check_client(client):
    cli = Client.objects.get(name=str(client))
    return list(Project.objects.get(client=cli))

def check_department(dept):
    depart = Department.objects.get(name=str(dept))
    return list(Project.objects.get(department=depart))

def check_type(proj_type):
    proj = Type.objects.get(name=str(proj_type))
    return list(Project.objects.get(type=proj))

def generate_report(req):
    report = list()
    report += check_dates(req['start_date'], req['end_date'])
    report += check_semester(req['semester'])
    report += check_user(req['user'])
    report += check_department(req['department'])
    report += check_type(req['proj_type'])
    report += check_client(req['client'])
    return report
