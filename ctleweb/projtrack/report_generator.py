from datetime import datetime

from .models import Project, Semester, User, Client, Department, Type

from django.core.exceptions import ObjectDoesNotExist

def remove_duplicates(t):
    l = []
    for x in t:
        if x not in l:
            l.append(x)
    return l

def check_dates(s_d, e_d):
    try:
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
    except ObjectDoesNotExist:
        return []

def check_semester(sem):
    try:
        if sem != '':
            try:
                return list(Project.objects.get(semester=sem))
            except TypeError:
                return Project.objects.get(semester=sem)
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return Project.objects.all()
    except ObjectDoesNotExist:
        return []

def check_user(use):
    try:
        if use != '':
            #use = User.objects.get(username=str(user))
            return list(Project.objects.get(users=use))
        else:
            return list(Project.objects.all())
    except ObjectDoesNotExist:
        return []

def check_client(cli):
    try:
        if cli != '':
            try:
                return list(Project.objects.get(client=cli))
            except TypeError:
                return Project.objects.get(client=cli)
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return Project.objects.all()
    except ObjectDoesNotExist:
        return []

def check_department(depart):
    try:
        if depart != '':
            try:
                cli = Client.objects.get(department=depart)
                return list(Project.objects.get(client=cli))
            except TypeError:
                cli = Client.objects.get(department=depart)
                return Project.objects.get(client=cli)
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return Project.objects.all()
    except ObjectDoesNotExist:
        return []

def check_type(proj):
    try:
        if proj != '':
            try:
                return list(Project.objects.get(type=proj))
            except TypeError:
                return Project.objects.get(type=proj)
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return Project.objects.all()
    except ObjectDoesNotExist:
        return []

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
