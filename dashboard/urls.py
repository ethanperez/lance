from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('dashboard.views',
    #url(r'^$', views.dashboard, name = 'dashboard'),
    url(r'^login/$', views.viewLogin, name = 'login'),
    url(r'^logout/$', views.viewLogout, name = 'logout'),
)
