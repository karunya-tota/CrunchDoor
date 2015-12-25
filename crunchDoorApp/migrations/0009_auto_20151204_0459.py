# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0008_auto_20151204_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunch',
            name='founded',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='crunch',
            name='funding',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
