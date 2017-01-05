from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'projtrack'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
