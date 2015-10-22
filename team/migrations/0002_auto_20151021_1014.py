# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address_zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
