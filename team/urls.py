from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('team.views',
    # Rides
    url(r'stats/$', views.fitnessStats, name = 'stats'),
    url(r'directory/$', views.teamDirectory, name = 'directory')
)