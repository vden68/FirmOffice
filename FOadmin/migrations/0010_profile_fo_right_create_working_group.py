# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0009_workinggrouppartner_fo_working_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fo_right_create_working_group',
            field=models.BooleanField(default=False, verbose_name='Право на создание рабочей группы'),
        ),
    ]
