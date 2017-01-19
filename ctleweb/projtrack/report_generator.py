from datetime import datetime

from .models import Project, Semester, User, Client, Department, Type

def remove_duplicates(t):
    l = []
    for x in t:
        if x not in l:
            l.append(x)
    return l

def check_dates(s_d, e_d):
    result = list(Project.objects.all())
    if s_d != '':
        s_d = datetime.strptime(s_d, "%Y-%m-%d")
        for x in result:
            if x.date > s_d:
                result.remove(x)
    if e_d != '':
        e_d = datetime.strptime(e_d, "%Y-%m-%d")
        for x in result:
            if x.date < e_d:
                result.remove(x)
    return result

def check_semester(semester):
    if semester != '':
        sem = Semester.objects.get(name=str(semester))
        return list(Project.objects.get(semester=sem))
    else:
        return list(Project.objects.all())

def check_user(user):
    if user != '':
        use = User.objects.get(username=str(user))
        return list(Project.objects.get(users=use))
    else:
        return list(Project.objects.all())

def check_client(cli):
    if cli != '':
        #cli = Client.objects.get(name=str(client))
        return list(Project.objects.get(client=cli))
    else:
        return list(Project.objects.all())

def check_department(dept):
    if dept != '':
        depart = Department.objects.get(name=str(dept))
        return list(Project.objects.get(department=depart))
    else:
        return list(Project.objects.all())

def check_type(proj_type):
    if proj_type != '':
        proj = Type.objects.get(name=str(proj_type))
        return list(Project.objects.get(type=proj))
    else:
        return list(Project.objects.all())

def generate_report(req):
    report = list()
    report += check_dates(req['start_date'], req['end_date'])
    report += check_semester(req['semester'])
    report += check_user(req['user'])
    report += check_department(req['department'])
    report += check_type(req['proj_type'])
    report += check_client(req['client'])
    report = remove_duplicates(report)
    return report
