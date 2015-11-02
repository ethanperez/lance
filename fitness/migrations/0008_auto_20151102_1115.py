# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0007_auto_20151102_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='first_aid',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='injuries',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='responders',
            field=models.TextField(blank=True, verbose_name='who responded to the incident? (include all parties - Riders, Paramedics, Police, etc.)'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='witnesses',
            field=models.TextField(blank=True),
        ),
    ]
