# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20151021_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='site_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
