# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
