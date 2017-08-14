# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20170807_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='patch_id',
        ),
        migrations.RenameField(
            model_name='patch',
            old_name='upload_time',
            new_name='update_time',
        ),
        migrations.AddField(
            model_name='patch',
            name='apply_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patch',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patch',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patch',
            name='is_enable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patch',
            name='is_gray',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patch',
            name='pool_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patch',
            name='serial_number',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Release',
        ),
    ]