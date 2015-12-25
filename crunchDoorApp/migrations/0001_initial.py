# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_id', models.IntegerField(max_length=10)),
                ('numberofEmployees', models.IntegerField(max_length=20)),
                ('date_founded', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=50)),
                ('total_funding', models.IntegerField(max_length=20)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('email_address', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lattitude', models.DecimalField(max_digits=10, decimal_places=4)),
                ('longitutde', models.DecimalField(max_digits=10, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_Reviews', models.IntegerField(verbose_name=15)),
                ('average', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
        ),
    ]
