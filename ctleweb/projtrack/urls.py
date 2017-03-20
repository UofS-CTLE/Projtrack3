from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'projtrack'
urlpatterns = [
    url(r'^projtrack3/$', views.index, name='index'),
    url(r'^projtrack3/index/$', views.index, name='index'),
    url(r'^projtrack3/home/$', views.home, name='home'),
    url(r'^projtrack3/add_project/$', views.add_project, name='add_project'),
    url(r'^projtrack3/add_client/$', views.add_client, name='add_client'),
    url(r'^projtrack3/client_view/$', views.client_view, name='client_view'),
    url(r'^projtrack3/add_department/$', views.add_department, name='add_department'),
    url(r'^projtrack3/add_type/$', views.add_type, name='add_type'),
    url(r'^projtrack3/report_page/$', views.report_page, name='report_page'),
    url(r'^projtrack3/all_projects/$', views.all_projects, name='all_projects'),
    url(r'^projtrack3/my_projects/$', views.my_projects, name='my_projects'),
    url(r'^projtrack3/not_logged_in/$', views.not_logged_in, name='not_logged_in'),
    url(r'^projtrack3/logout/$', views.logout_view, name='logout'),
    url(r'^projtrack3/issues/$', views.issues, name='issues'),
]
