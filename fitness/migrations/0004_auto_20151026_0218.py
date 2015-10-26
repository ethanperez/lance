# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_incident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='group_members',
        ),
        migrations.AddField(
            model_name='ride',
            name='group_members',
            field=models.CharField(default='Ethan', max_length=200),
            preserve_default=False,
        ),
    ]
