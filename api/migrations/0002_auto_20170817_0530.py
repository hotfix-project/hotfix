# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patch',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Released'), (4, 'Stoped'), (3, 'PreReleased'), (0, 'Deleted')], default=1),
        ),
    ]
