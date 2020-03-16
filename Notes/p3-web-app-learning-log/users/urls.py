"""Defines URL patterns for users"""
from django.conf.urls import url
# from django.contrib.auth.views import login
# this is obsolete, instead use
from django.contrib.auth import views as auth_views

from . import views

app_name = "users" # include() requires app_name

urlpatterns = [
    # Login page
    url('^login/', auth_views.LoginView.as_view(extra_context={'title': "Log in"}, template_name='users/login.html'), name="login"),
    # Logout page
    url('^logout/', views.logout_view, name="logout"),
    # Registration page
    url(r'^register/$', views.register, name='register'),
]