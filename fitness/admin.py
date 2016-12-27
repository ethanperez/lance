from django.contrib import admin
from django.utils.html import format_html
from .models import Ride, Incident

# Settings for ride admin
class RideAdmin(admin.ModelAdmin):

  list_display = ('member', 'group_members', 'date', 'duration', 'miles', 'pace', 'logged')
  list_filter = ('date', 'logged')
  search_fields = ('member__first_name', 'member__last_name')
  ordering = ('-logged', '-date')

admin.site.register(Ride, RideAdmin)

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'date_logged', 'incident_date', 'follow_up', 'read', 'pdf_url')
    list_filter = ('date_logged', 'incident_date')
    search_fields = ('member__first_name', 'member__first_name', 'follow_up',)
    ordering = ('-date_logged', '-incident_date')

    def pdf_url(self, obj):
        return format_html("<a href='/fitness/incidents/{id}/pdf/'>{id}</a>", id = obj.id)

    pdf_url.short_description = "PDF Link"

admin.site.register(Incident, IncidentAdmin)
