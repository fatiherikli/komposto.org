# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sketches', '0004_auto_20170424_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketch',
            name='fork_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sketches.Sketch'),
        ),
    ]
