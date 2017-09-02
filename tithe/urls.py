from django.conf.urls import url
from tithe import views
from django.contrib.auth.views import (
    login, logout, password_reset, 
)
#from . import views

urlpatterns = [
    url(r'tithe/$', views.offerings_add, name='offerings_add'),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^accounts/profile/$', views.view_profile, name='profile'),
    #url(r'^account/profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]