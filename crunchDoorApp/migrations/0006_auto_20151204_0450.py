# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0005_auto_20151204_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunch',
            name='symbol',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
