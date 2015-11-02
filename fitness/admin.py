from django.contrib import admin
from .models import Ride, Incident

# Settings for ride admin
class RideAdmin(admin.ModelAdmin):

  list_display = ('member', 'group_members', 'date', 'duration', 'miles', 'pace', 'logged')
  list_filter = ('date', 'logged')
  search_fields = ('rider__first_name', 'rider__last_name')
  ordering = ('-logged', '-date')

admin.site.register(Ride, RideAdmin)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'date_logged', 'incident_date', 'follow_up', 'read')
    list_filter = ('date_logged', 'incident_date')
    ordering = ('-date_logged', '-incident_date')

admin.site.register(Incident, IncidentAdmin)