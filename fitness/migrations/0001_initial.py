# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=datetime.datetime(2015, 10, 22, 18, 26, 58, 390305, tzinfo=utc))),
                ('miles', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pace', models.DecimalField(decimal_places=2, max_digits=4)),
                ('duration', models.DurationField()),
                ('comments', models.TextField()),
                ('logged', models.DateTimeField(auto_now_add=True)),
                ('group_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='group')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='name', related_name='rider')),
            ],
        ),
    ]
