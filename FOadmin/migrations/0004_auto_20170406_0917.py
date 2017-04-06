# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('FOadmin', '0003_auto_20170404_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystructure',
            name='fo_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.ProtectedError, to='FOadmin.Department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='companystructure',
            name='title',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True, verbose_name='Название'),
        ),
    ]
