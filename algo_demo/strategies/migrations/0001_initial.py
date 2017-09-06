# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('symbol', models.CharField(max_length=250)),
                ('isin', models.CharField(max_length=100)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.Industry')),
            ],
        ),
    ]
