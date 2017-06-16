# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0011_user_correct_answered'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_bonus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='correct_answered',
            field=models.IntegerField(default=5),
        ),
    ]
