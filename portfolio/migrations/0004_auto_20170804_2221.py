# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20170804_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Web', 'Web'), ('Programm', 'Programm'), ('Bots', 'Bots'), ('Mobile App', 'Mobile Apps')], max_length=10),
        ),
    ]