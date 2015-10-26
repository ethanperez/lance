from django.contrib import admin
from .models import Ride, Incident

# Settings for ride admin
class RideAdmin(admin.ModelAdmin):

  list_display = ('member', 'get_group_members', 'date', 'duration', 'miles', 'pace', 'logged')
  list_filter = ('date', 'logged')
  search_fields = ('rider__first_name', 'rider__last_name')
  ordering = ('-logged', '-date')

admin.site.register(Ride, RideAdmin)
admin.site.register(Incident)