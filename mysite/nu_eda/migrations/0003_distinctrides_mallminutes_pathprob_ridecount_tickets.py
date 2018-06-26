# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nu_eda', '0002_auto_20171203_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistinctRides',
            fields=[
                ('distinct_rides', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_count', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'distinct_rides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MallMinutes',
            fields=[
                ('miniutes_in_mall', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_count', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mall_minutes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PathProb',
            fields=[
                ('ride1', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ride2', models.CharField(max_length=50)),
                ('cust_count', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'path_prob',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RideCount',
            fields=[
                ('no_of_rides', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_count', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ride_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_type', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('ticketname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('size', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tickets',
                'managed': False,
            },
        ),
    ]