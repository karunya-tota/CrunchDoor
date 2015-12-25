# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0007_auto_20151204_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunch',
            name='employees',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
