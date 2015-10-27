# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_auto_20151026_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='date',
            field=models.DateField(),
        ),
    ]
