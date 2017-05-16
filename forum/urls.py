from django.conf.urls import url, include

from .views import read_topic, action_topic, SetFilter, index

urlpatterns = [

    url(r'^dashboard/$', index, name='index'),    
    url(r'^$', read_topic, name='read_topic'),
    url(r'^action_topic/$', action_topic, name='action_topic'),
    url(r'^SetFilter/$', SetFilter, name='SetFilter'),

] 