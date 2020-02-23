"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
# must specify app_name to use include()

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # for each name
    # need to define function in views.py

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]