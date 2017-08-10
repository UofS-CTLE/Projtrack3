from datetime import datetime, date

from django.core.exceptions import ObjectDoesNotExist

from .models import Project, User, Client, Department, Type


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                tmp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = tmp
    return l


# noinspection PyUnresolvedReferences,PyUnresolvedReferences
def retrieve_most_recent_techcon(client):
    try:
        proj = list(Project.objects.filter(client=client))
        proj = bubble_sort(proj)
        return [proj.pop()]
    except TypeError:
        return [Project.objects.filter(client=client)]


# noinspection PyUnresolvedReferences,PyUnresolvedReferences
def check_dates(s_d, e_d):
    try:
        result = list(Project.objects.all())
        ret = []
        if s_d != '' and e_d != '':
            s_d = datetime.strptime(s_d, "%m/%d/%Y").date()
            e_d = datetime.strptime(e_d, "%m/%d/%Y").date()
            for x in result:
                if s_d < x.date:
                    if e_d > x.date:
                        ret.append(x)
            return ret
        elif s_d != '' and e_d == '':
            s_d = datetime.strptime(s_d, "%m/%d/%Y").date()
            for x in result:
                d = x.date
                if d > s_d:
                    ret.append(x)
            return ret
        elif s_d == '' and e_d != '':
            e_d = datetime.strptime(e_d, "%m/%d/%Y").date()
            for x in result:
                if x.date < e_d:
                    ret.append(x)
            return ret
        elif e_d == '' and s_d == '':
            return list(Project.objects.all())
        else:
            return []
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
def check_semester(sem):
    try:
        if sem != '':
            try:
                return list(Project.objects.filter(semester=sem))
            except TypeError:
                return [Project.objects.filter(semester=sem)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
def check_user(use):
    try:
        if use != '':
            try:
                return list(Project.objects.filter(users=use))
            except TypeError:
                return [Project.objects.filter(users=use)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
def check_client(cli):
    try:
        if cli != '':
            try:
                return list(Project.objects.filter(client=cli))
            except TypeError:
                return [Project.objects.filter(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,
# noinspection PyUnresolvedReferences,PyUnresolvedReferences
def check_department(depart):
    try:
        if depart != '':
            try:
                cli = Client.objects.filter(department=depart)
                return list(Project.objects.filter(client=cli))
            except TypeError:
                cli = Client.objects.filter(department=depart)
                return [Project.objects.filter(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
def check_type(proj):
    try:
        if proj != '':
            try:
                return list(Project.objects.filter(type=proj))
            except TypeError:
                return [Project.objects.filter(type=proj)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []


# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,
# noinspection PyUnresolvedReferences
def generate_stats(report):
    hours = 0
    walk_ins = 0
    projects = len(report)
    users = dict()
    for x in report:
        hours += x.hours
        if x.walk_in:
            walk_ins += 1
    for x in list(User.objects.filter(is_active=True)):
        proj = 0
        hour = 0
        for y in list(Project.objects.all()):
            if y.users.email == x.email:
                proj += 1
                hour += y.hours
        users[x.email] = {'projects': proj, 'hours': hour}
    depts = dict()
    for x in list(Department.objects.all()):
        proj = 0
        for y in list(Project.objects.all()):
            if y.client.department.name == x.name:
                proj += 1
        depts[x.name] = proj
    types = dict()
    for x in list(Type.objects.all()):
        proj = 0
        for y in list(Project.objects.all()):
            if y.type == x:
                proj += 1
        types[x.name] = proj
    try:
        walk_in_percent = ((float(walk_ins) / float(projects)) * 100)
    except ZeroDivisionError:
        walk_in_percent = 0
    try:
        stats = {
            'active_devs': len(users),
            'average_proj': projects // len(users),
            'average_hour': hours / len(users)
        }
    except ZeroDivisionError:
        stats = {
            'active_devs': 0,
            'average_proj': 0,
            'average_hour': 0
        }
    date_v = str(date.today())
    report = {
        'date': date_v,
        'total_projects': projects,
        'total_hours': hours,
        'walk_ins': walk_ins,
        'walk_in_percent': walk_in_percent,
        'users': users,
        'depts': depts,
        'types': types,
        'stats': stats
    }
    return report


# noinspection PyUnresolvedReferences
def generate_report(req):
    proj_list = set(list(Project.objects.all()))
    rep = [
        (set(check_dates(req['start_date'], req['end_date']))),
        (set(check_semester(req['semester']))),
        (set(check_user(req['user']))),
        (set(check_department(req['department']))),
        (set(check_type(req['proj_type']))),
        (set(check_client(req['client'])))
    ]
    for x in rep:
        proj_list = proj_list & x
    if req['sort_by_date']:
        proj_list = bubble_sort(list(proj_list))
    report = generate_stats(proj_list)
    report['project_list'] = proj_list
    return report
