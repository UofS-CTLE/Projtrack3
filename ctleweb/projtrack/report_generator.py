from datetime import datetime

import os

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Project, Client


class UserStats(object):
    def __init__(self, user):
        self.user_object = user
        self.name = user.username
        self.projects_list = list(Project.objects.filter(users=self.user_object))
        self.projects_count = 0
        self.projects_hours = 0

    def update_stats(self):
        self.projects_count = len(self.projects_list)
        for x in self.projects_list:
            self.projects_hours += x.hours


class Report(object):
    def __init__(self, request):
        self.date = datetime.today().strftime("%m/%d/%Y")
        self.semester = request['semester']
        self.total_projects = 0
        self.total_hours = 0
        self.walk_ins = 0
        self.percent_walk_in = 0
        self.active_user_list = list(User.objects.filter(is_active=True))
        self.user_objects_list = list()
        self.start_date = request['start_date']
        self.end_date = request['end_date']
        self.user = request['user']
        self.client = request['client']
        self.department = request['department']
        self.project_type = request['proj_type']
        self.user_list()
        self.filter_projects()
        for x in self.user_objects_list:
            x.update_stats()
        self.report_string = ''
        self.create_report()
        self.write_report()

    def user_list(self):
        if self.user == '':
            request = self.active_user_list
        else:
            request = [self.user]
        for x in request:
            self.user_objects_list.append(UserStats(x))

    def filter_projects(self):
        for x in self.user_objects_list:
            results = []
            if self.start_date != '0/0/0' or self.end_date != '0/0/0':
                results.append(set(check_dates(self.start_date, self.end_date)))
            if self.user != '':
                results.append(set(check_user(self.user)))
            if self.client != '':
                results.append(set(check_client(self.client)))
            if self.department != '':
                results.append(set(check_department(self.department)))
            if self.project_type != '':
                results.append(set(check_type(self.project_type)))
            for z in results:
                x.projects_list = list(set(x.projects_list) & z)

    def create_report(self):
        self.report_string = '<!DOCTYPE html><html><head><title>Report ' + str(self.date) + '</title>'
        self.report_string += '<style> table, th, td { border: 1px solid black; padding: 5px; }</style></head>'
        self.report_string += 'Semester: '
        if self.semester == '':
            self.report_string += 'All'
        else:
            self.report_string += str(self.semester)
        self.report_string += '<br/>'
        self.report_string += "</body></html>"

    def write_report(self):
        with open(os.path.join(settings.BASE_DIR, 'projtrack/templates/projtrack/report_page.html'), 'w') as f:
            f.write(self.report_string)
            f.close()


def check_dates(s_d, e_d):
    try:
        result = list(Project.objects.all())
        ret = []
        if s_d != '0/0/0' and e_d != '0/0/0':
            s_d = datetime.strptime(s_d, "%m/%d/%Y").date()
            e_d = datetime.strptime(e_d, "%m/%d/%Y").date()
            for x in result:
                if s_d < x.date:
                    if e_d > x.date:
                        ret.append(x)
            return ret
        elif s_d != '0/0/0' and e_d == '0/0/0':
            s_d = datetime.strptime(s_d, "%m/%d/%Y").date()
            for x in result:
                d = x.date
                if d > s_d:
                    ret.append(x)
            return ret
        elif s_d == '0/0/0' and e_d != '0/0/0':
            e_d = datetime.strptime(e_d, "%m/%d/%Y").date()
            for x in result:
                if x.date < e_d:
                    ret.append(x)
            return ret
        elif e_d == '0/0/0' and s_d == '0/0/0':
            return list(Project.objects.all())
        else:
            return []
    except ObjectDoesNotExist:
        return []


def check_semester(sem):
    try:
        try:
            return list(Project.objects.filter(semester=sem))
        except TypeError:
            return [Project.objects.filter(semester=sem)]
    except ObjectDoesNotExist:
        return []


def check_user(use):
    try:
        try:
            return list(Project.objects.filter(users=use))
        except TypeError:
            return [Project.objects.filter(users=use)]
    except ObjectDoesNotExist:
        return []


def check_client(cli):
    try:
        try:
            return list(Project.objects.filter(client=cli))
        except TypeError:
            return [Project.objects.filter(client=cli)]
    except ObjectDoesNotExist:
        return []


def check_department(depart):
    try:
        try:
            cli = Client.objects.filter(department=depart)
            return list(Project.objects.filter(client=cli))
        except TypeError:
            cli = Client.objects.filter(department=depart)
            return [Project.objects.filter(client=cli)]
    except ObjectDoesNotExist:
        return []


def check_type(proj):
    try:
        try:
            return list(Project.objects.filter(type=proj))
        except TypeError:
            return [Project.objects.filter(type=proj)]
    except ObjectDoesNotExist:
        return []
