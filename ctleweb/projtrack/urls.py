from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'projtrack3'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^client_view/$', views.client_view, name='client_view'),
    url(r'^add_department/$', views.add_department, name='add_department'),
    url(r'^add_type/$', views.add_type, name='add_type'),
    url(r'^report_page/$', views.report_page, name='report_page'),
    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^my_projects/$', views.my_projects, name='my_projects'),
    url(r'^not_logged_in/$', views.not_logged_in, name='not_logged_in'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^issues/$', views.issues, name='issues'),
]
