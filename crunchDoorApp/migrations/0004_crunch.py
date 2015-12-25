# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0003_auto_20151201_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permalink', models.CharField(max_length=150)),
                ('founded', models.CharField(max_length=150)),
                ('employes', models.IntegerField(default=0)),
                ('funding', models.IntegerField(default=0)),
                ('symbol', models.CharField(default=b'0', max_length=200)),
            ],
        ),
    ]
