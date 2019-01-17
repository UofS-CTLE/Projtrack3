from django.conf.urls import url

from . import views

app_name = 'projtrack3'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index')
]
