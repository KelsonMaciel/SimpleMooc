# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 16:03
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170913_1307'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
