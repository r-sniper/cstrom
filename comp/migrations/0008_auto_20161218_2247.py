# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0007_auto_20161217_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
