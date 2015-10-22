# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(verbose_name='email address', db_index=True, unique=True, max_length=100)),
                ('first_name', models.CharField(verbose_name='first name', max_length=35)),
                ('last_name', models.CharField(verbose_name='last name', max_length=35)),
                ('route', models.CharField(max_length=8, choices=[('none', 'None (staff)'), ('sierra', 'Sierra'), ('rockies', 'Rockies'), ('ozarks', 'Ozarks')], default='none')),
                ('date_of_birth', models.DateField(verbose_name='date of birth', blank=True, null=True)),
                ('is_active', models.BooleanField(verbose_name='active status', default=True)),
                ('is_rider', models.BooleanField(verbose_name='is on current team', default=True)),
                ('is_staff', models.BooleanField(verbose_name='member of leadership', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('site_rider_url', models.CharField(max_length=200, blank=True)),
                ('site_photo_url', models.URLField(blank=True)),
                ('phone', models.BigIntegerField(blank=True)),
                ('address_line1', models.CharField(max_length=100, blank=True)),
                ('address_line2', models.CharField(max_length=100, blank=True)),
                ('address_zip', models.IntegerField(blank=True)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups', blank=True, related_query_name='user', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions', blank=True, related_query_name='user', related_name='user_set')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
    ]
