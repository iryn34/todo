from django.conf.urls import url

from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<task_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<task_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
