# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170804_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('web', 'Web'), ('programm', 'Programm'), ('bots', 'Bots'), ('mobile_app', 'Mobile Apps')], max_length=10),
        ),
    ]
