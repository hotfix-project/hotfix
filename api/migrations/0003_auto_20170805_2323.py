# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_patch_local_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patch',
            old_name='local_url',
            new_name='download_url',
        ),
    ]