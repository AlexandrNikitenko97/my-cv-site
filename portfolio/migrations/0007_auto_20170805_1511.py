# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_link',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
