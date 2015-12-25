# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0002_auto_20151201_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.CharField(default=b'0', max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(default=b'0', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(default=b'0', max_length=100),
        ),
    ]
