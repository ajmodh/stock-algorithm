# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.CharField(max_length=250)),
                ('params', models.TextField()),
                ('profit', models.FloatField()),
                ('average', models.FloatField()),
                ('winrate', models.FloatField()),
                ('trades', models.FloatField()),
                ('holding_periods', models.FloatField()),
                ('default', models.BooleanField(default=False)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.Stock')),
            ],
        ),
    ]