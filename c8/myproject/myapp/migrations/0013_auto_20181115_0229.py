# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-14 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20181115_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbom',
            name='additionalDetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product'),
        ),
    ]
