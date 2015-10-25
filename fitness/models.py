from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from team.models import Member

class Ride(models.Model):
  member = models.ForeignKey(Member, verbose_name = 'name', related_name = 'rider')
  date = models.DateField(auto_now_add = True)
  group_members = models.ManyToManyField(Member, related_name = 'group')
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