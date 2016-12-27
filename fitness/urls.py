from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('fitness.views',
    # Rides
    url(r'^rides/$', views.viewAllRides, name = 'allRides'),
    url(r'^rides/add/$', views.logRide, name = 'logRide'),
    # Incidents
    url(r'^incidents/$', views.viewAllIncidents, name = 'allIncidents'),
    url(r'^incidents/add/$', views.logIncident, name = 'logIncident'),
    url(r'incidents/(?P<incident>\d+)$', views.viewIncident, name='viewIncident'),
    url(r'incidents/(?P<incident>\d+)/pdf/$', views.viewIncidentPdf, name='viewIncidentPdf')
)
