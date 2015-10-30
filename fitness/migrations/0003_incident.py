# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0002_auto_20151022_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=2, choices=[('nm', 'Near Miss'), ('ac', 'Accident')])),
                ('date_logged', models.DateTimeField(auto_now_add=True)),
                ('event', models.CharField(max_length=100)),
                ('incident_date', models.DateTimeField()),
                ('incident_location', models.CharField(max_length=100, verbose_name='location of incident')),
                ('incident_description', models.TextField(verbose_name='provide full description of all events leading up to and including the incident')),
                ('surrounding_description', models.TextField(verbose_name='provide full description of all events leading up to and including the incident')),
                ('witnesses', models.extField()),
                ('responders', models.TextField(verbose_name='who responded to the incident? (include all parties - Riders, Paramedics, Police, etc.)')),
                ('injuries', models.TextField()),
                ('follow_up', models.TextField(verbose_name='description of follow up action')),
                ('member', models.ForeignKey(verbose_name='name', related_name='incident_rider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
