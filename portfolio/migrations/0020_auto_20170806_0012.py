# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20170805_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Web', 'Web'), ('Program', 'Program'), ('Bots', 'Bots'), ('Mobile App', 'Mobile App')], max_length=10),
        ),
    ]
