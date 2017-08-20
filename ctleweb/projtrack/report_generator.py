from datetime import datetime

from .models import User, Project


class UserStats(object):
    def __init__(self, user):
        self.user_object = user
        self.name = user.username
        self.projects_list = list(Project.object.filter(user=self.user_object))
        self.projects_count = len(self.projects_list)


class Report(object):
    def __init__(self, request):
        self.date = datetime.today().strftime("%m/%d/%Y")
        self.semester = request['semester']
        self.total_projects = 0
        self.total_hours = 0
        self.walk_ins = 0
        self.percent_walk_in = 0
        self.active_user_list = list(User.objects.filter(is_active=True))
        self.start_date = request['start_date']
        self.end_date = request['end_date']
        self.user = request['user']
        self.client = request['client']
        self.department = request['department']
        self.project_type = request['proj_type']
        self.user_list()

    def user_list(self):
        if self.user == '':
            request = self.active_user_list
        else:
            request = [self.user]
        for x in request:
            y = UserStats(x)
