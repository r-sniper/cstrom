# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0006_auto_20161217_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='count',
            new_name='count_easy',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='question_array',
            new_name='question_array_easy',
        ),
        migrations.AddField(
            model_name='user',
            name='count_hard',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='count_medium',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='question_array_hard',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='question_array_medium',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
