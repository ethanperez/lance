from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('fitness.views',
    url(r'^rides/$', views.viewAllRides, name = 'allRides'),
    url(r'^rides/add/$', views.logRide, name = 'logRide'),
    url(r'^incidents/$', views.viewAllIncidents, name = 'allIncidents'),
    url(r'^incidents/add/$', views.logIncident, name = 'logIncident'),

)