# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='technologies',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(),
        ),
    ]
