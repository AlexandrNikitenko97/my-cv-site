# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20170805_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_link',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]