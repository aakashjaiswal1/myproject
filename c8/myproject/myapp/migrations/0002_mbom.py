# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-14 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mbom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionalDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
                ('ebom1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Ebom')),
            ],
        ),
    ]
