# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 11:05
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0013_remove_profile_fo_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fo_user_photo',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/fo_user'), upload_to=''),
        ),
    ]
