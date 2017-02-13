# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0006_auto_20170213_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fo_user_last_name',
            field=models.CharField(default='-', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fo_user_name',
            field=models.CharField(default='-', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fo_user_patronymic',
            field=models.CharField(default='-', max_length=50, verbose_name='Отчество'),
        ),
    ]
