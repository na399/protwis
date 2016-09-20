# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('mutation', '0002_auto_20160901_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='mutationexperiment',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='common.Publication'),
        ),
    ]