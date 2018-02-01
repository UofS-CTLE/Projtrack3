import os
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Project, Client, Semester, Department, Type


class UserStats(object):
    def __init__(self, user):
        try:
            self.user_object = User.objects.get(username=user)
        except ObjectDoesNotExist:
            self.user_object = User.objects.get(pk=user)
        self.name = self.user_object.username
        self.projects_list = list(Project.objects.filter(users=self.user_object))
        self.projects_count = 0
        self.projects_hours = 0
        self.walk_in = 0

    def update_stats(self):
        self.projects_count = len(self.projects_list)
        for x in self.projects_list:
            self.projects_hours += x.hours
            if x.walk_in:
                self.walk_in += 1


class Report(object):
    def __init__(self, request):
        self.date = datetime.today().strftime("%m/%d/%Y")
        try:
            self.semester = Semester.objects.get(pk=int(request['semester']))
        except ValueError:
            self.semester = ''
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
        self.stats = request['stats']
        self.user_list()
        self.filter_projects()
        for x in self.user_objects_list:
            x.update_stats()
            self.total_projects += x.projects_count
            self.total_hours += x.projects_hours
            self.walk_ins += x.walk_in
        if self.total_projects != 0:
            self.percent_walk_in = (float(self.walk_ins) / float(self.total_projects)) * 100
        else:
            self.percent_walk_in = 0
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
            if self.semester != '':
                results.append(set(check_semester(self.semester)))
            for z in results:
                x.projects_list = list(set(x.projects_list) & z)

    def create_report(self):
        self.report_string = '<!DOCTYPE html><html><head><title>Report ' + str(self.date) + '</title>'
        self.report_string += '<style> table, th, td { border: 1px solid black; padding: 5px; font-size: 10pt; }' \
                              '</style></head>'
        self.report_string += '<body><h1>Project Report</h1>'
        self.report_string += '''<a href="{% url 'projtrack3:report_page' %}">
                                 Return to the report generation page.</a><br/><br/>Date: ''' + str(self.date)
        self.report_string += '<br/>Semester: '
        if self.semester == '':
            self.report_string += 'All'
        else:
            self.report_string += str(self.semester)
        self.report_string += '<br/>Total Projects: ' + str(self.total_projects)
        self.report_string += '<br/>Total Hours: ' + str(self.total_hours)
        self.report_string += '<br/>Walk-ins: ' + str(self.walk_ins) + ' (' + str(self.percent_walk_in) + '%)'
        self.report_string += '<br/>Active Developers : ' + str(len(self.active_user_list)) + "<br/><br/>"

        if self.stats:
            project_list = []
            for x in self.user_objects_list:
                for y in x.projects_list:
                    project_list.append(y)
            report = generate_stats(project_list)
            assert isinstance(report, dict)
            for x, y in report.items():
                self.report_string += str(x)
                self.report_string += '<table>'
                if str(x) == 'Users':
                    self.report_string += '<tr><td>Name</td><td>Hours</td><td>Projects</td></tr>'
                    for z, a in y.items():
                        self.report_string += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(str(z), a['hours'],
                                                                                                  a['projects'])
                else:
                    for z, a in y.items():
                        self.report_string += '<tr><td>{}</td><td>{}</td></tr>'.format(str(z), str(a))
                self.report_string += '</table><br/>'

        for x in self.user_objects_list:
            if x.projects_count != 0:
                self.report_string += '<strong>{} {}; {} total projects.</strong>'.format(x.user_object.first_name,
                                                                                          x.user_object.last_name,
                                                                                          x.projects_count)
                self.report_string += '''<table><tr><td>Title</td><td>Client</td><td>Developer</td><td>Hours</td><td>Date</td>
                                  <td>Description</td><td>Completed Status</td></tr>'''
                for y in x.projects_list:
                    name = ""
                    for u in y.users.all():
                        name += u.first_name + " " + u.last_name + ", "
                    self.report_string += '''<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>
                                         <td>{}</td><td>{done}</td></tr>'''.format(y.title, y.client,
                                                                                   name,
                                                                                   y.hours, y.date, y.description,
                                                                                   done="&#x2714;"
                                                                                   if y.completed else '')
                self.report_string += '</table><br>'
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


def generate_stats(report):
    hours = 0
    walk_ins = 0
    users = dict()
    projects = list(Project.objects.all())
    active = list(User.objects.filter(is_active=True))
    for x in report:
        hours += x.hours
        if x.walk_in:
            walk_ins += 1
    ##############################################################################
    # PERFORMANCE BOTTLENECK
    # This block is the problem. We're essentially in a triply-nested loop.
    # We'll need to see if we can flatten this out a bit.
    # This block is taking approximately 30 seconds to generate a stats report.
    for x in active:
        proj = 0
        hour = 0
        for y in projects:
            if x in y.users.all():
                proj += 1
                hour += y.hours
        users[x.email] = {'projects': proj, 'hours': hour}
    ##############################################################################
    depts = dict()
    for x in list(Department.objects.all()):
        proj = 0
        for y in projects:
            if y.client.department.name == x.name:
                proj += 1
        depts[x.name] = proj
    types = dict()
    for x in list(Type.objects.all()):
        proj = 0
        for y in projects:
            if y.type == x:
                proj += 1
        types[x.name] = proj
    report_dict = {
        'Users': users,
        'Projects per Department': depts,
        'Projects per Type': types
    }
    return report_dict
