# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-23 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181223_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordinarymember',
            old_name='user',
            new_name='用户',
        ),
        migrations.AlterField(
            model_name='ordinarymember',
            name='生日',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
