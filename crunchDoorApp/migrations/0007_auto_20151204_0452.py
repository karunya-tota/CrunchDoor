# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0006_auto_20151204_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunch',
            name='symbol',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
