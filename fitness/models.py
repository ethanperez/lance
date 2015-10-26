from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.utils import timezone
from datetime import datetime, timedelta
from team.models import Member

class Ride(models.Model):
  member = models.ForeignKey(Member, verbose_name = 'name', related_name = 'rider')
  date = models.DateField(auto_now_add = True)
  group_members = models.CharField(max_length = 200)
  miles = models.DecimalField(max_digits = 5, decimal_places = 2)
  pace = models.DecimalField(max_digits = 4, decimal_places = 2)
  duration = models.DurationField()
  comments = models.TextField(blank = False)
  logged = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return "{0}; {1}; {2}".format(self.member, self.miles, self.date)

  def get_group_members(self):
    return ", ".join([r.get_full_name() for r in self.group_members.all()])
  get_group_members.short_description = 'Group members'

class Incident(models.Model):
  TYPE_CHOICES = (
    ('nm', 'Near Miss'),
    ('ac', 'Accident'),
  )

  type = models.CharField(max_length = 2, choices = TYPE_CHOICES)
  member = models.ForeignKey(Member, verbose_name = 'name', related_name = 'incident_rider')
  date_logged = models.DateTimeField(auto_now_add = True)
  event = models.CharField(max_length = 100)
  incident_date = models.DateTimeField()
  incident_location = models.CharField('location of incident', max_length = 100)
  incident_description = models.TextField('provide full description of all events leading up to and including the incident')
  surrounding_description = models.TextField('provide full description of all events leading up to and including the incident')
  witnesses = HStoreField()
  responders = models.TextField('who responded to the incident? (include all parties - Riders, Paramedics, Police, etc.)')
  injuries = HStoreField()
  follow_up = models.TextField('description of follow up action')

  def __str__(self):
    return "{0} - {1}".format(self.member, self.incident_date)
