# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190729_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]