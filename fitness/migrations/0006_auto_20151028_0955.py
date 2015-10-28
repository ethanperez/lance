# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_auto_20151026_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='type',
        ),
        migrations.AddField(
            model_name='incident',
            name='first_aid',
            field=models.TextField(default='There was no first aid required'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='injuries',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='incident',
            name='witnesses',
            field=models.TextField(),
        ),
    ]
