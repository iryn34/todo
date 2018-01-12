from django.conf.urls import url

from . import views

app_name = 'contacts'
urlpatterns = [
    # ex: /polls/
    url(r'^\.(?P<format>[a-z]+)$', views.index, name='index'),

    # url(r'^(?P<contact_id>[0-9]+)/$', views.delete, name='delete'),

    url(r'^\/new$', views.new, name='new'),
    # ex: /polls/5/

    url(r'^\/(?P<contact_id>[0-9]+)\.(?P<format>[a-z]+)$', views.show, name='show'),

    # url(r'^(?P<contact_id>[0-9]+)/$', views.destroy, name='destroy'),

    url(r'^\/(?P<contact_id>[0-9]+)\/edit$', views.edit, name='edit'),

    # url(r'^(?P<contact_id>[0-9]+)/update/$', views.update, name='update'),
    # url(r'^specifics/(?P<contact_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<contact_id>[0-9]+)/results/$', views.results, name='results'),
]
