from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from . import views

app_name = 'projtrack3'

project_viewset = views.ProjectsSerializerView

client_viewset = views.ClientSerializerView

department_viewset = views.DepartmentSerializerView

type_viewset = views.TypeSerializerView

semester_viewset = views.SemesterSerializerView

router = routers.DefaultRouter()
router.register(r'users', views.UserSerializerView, base_name='User')
router.register(r'projects', project_viewset, base_name='Project')
router.register(r'clients', client_viewset, base_name='Client')
router.register(r'departments', department_viewset, base_name='Department')
router.register(r'types', type_viewset, base_name='Type')
router.register(r'semesters', semester_viewset, base_name='Semester')
router.register(r'current_semester', views.CurrentSemesterSerializerView, base_name="Current_Semester")

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^client_view/$', views.client_view, name='client_view'),
    url(r'^client_projects/(?P<id>\d+)/$', views.client_projects, name='client_projects'),
    url(r'^add_department/$', views.add_department, name='add_department'),
    url(r'^add_type/$', views.add_type, name='add_type'),
    url(r'^report_page/$', views.report_page, name='report_page'),
    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^my_projects/$', views.my_projects, name='my_projects'),
    url(r'^not_logged_in/$', views.not_logged_in, name='not_logged_in'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^issues/$', views.issues, name='issues'),
    url(r'^wiki/$', views.wiki, name='wiki'),
    url(r'^project_edit/$', views.edit_project, name='edit_project'),
    url(r'^project_edit/(?P<id>\d+)/$', views.edit_project, name='edit_project'),
    url(r'^project_delete/(?P<id>\d+)/$', views.project_delete, name='project_delete'),
    url(r'^api/', include(router.urls)),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
