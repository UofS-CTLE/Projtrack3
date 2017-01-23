from datetime import datetime

from .models import Project, Semester, User, Client, Department, Type

from django.core.exceptions import ObjectDoesNotExist

def check_dates(s_d, e_d):
    try:
        result = list(Project.objects.all())
        ret = []
        if s_d != '':
            s_d = datetime.strptime(s_d, "%Y-%m-%d").date()
            for x in result:
                if x.date > s_d:
                    ret.append(x)
        if e_d != '':
            e_d = datetime.strptime(e_d, "%Y-%m-%d").date()
            for x in result:
                if x.date < e_d:
                    ret.append(x)
        return ret
    except ObjectDoesNotExist:
        return []

def check_semester(sem):
    try:
        if sem != '':
            try:
                return list(Project.objects.get(semester=sem))
            except TypeError:
                return [Project.objects.get(semester=sem)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_user(use):
    try:
        if use != '':
            try:
                return list(Project.objects.get(users=use))
            except TypeError:
                return [Project.objects.get(users=use)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_client(cli):
    try:
        if cli != '':
            try:
                return list(Project.objects.get(client=cli))
            except TypeError:
                return [Project.objects.get(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
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
                return [Project.objects.get(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_type(proj):
    try:
        if proj != '':
            try:
                return list(Project.objects.get(type=proj))
            except TypeError:
                return [Project.objects.get(type=proj)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def generate_report(req):
    # TODO The sheer volume of memory we're using here is ridiculous.
    report = set(list(Project.objects.all())) 
    rep = [
            (set(check_dates(req['start_date'], req['end_date']))),
            (set(check_semester(req['semester']))),
            (set(check_user(req['user']))),
            (set(check_department(req['department']))),
            (set(check_type(req['proj_type']))),
            (set(check_client(req['client'])))
            ]
    for x in rep:
        report = report & x
    return report
