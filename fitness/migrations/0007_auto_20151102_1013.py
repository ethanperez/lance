# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0006_auto_20151028_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date_logged',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date logged'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='surrounding_description',
            field=models.TextField(verbose_name='please provide detailed description of surroundings, facility condition, weather condition, etc.'),
        ),
    ]
