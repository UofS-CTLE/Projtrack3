from django.conf.urls import url

from . import views

app_name = 'projtrack3'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^virtualClassroomStats/$', views.virtualClassroomStats, name='virtualClassroomStats'),
    url(r'^facultyNotUsingD2L/$', views.facultyNotUsingD2L, name='facultyNotUsingD2L')
]
