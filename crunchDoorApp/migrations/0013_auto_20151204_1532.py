# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0012_auto_20151204_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunch',
            name='similarcompany1',
            field=models.IntegerField(default=-1, max_length=50),
        ),
        migrations.AlterField(
            model_name='crunch',
            name='similarcompany2',
            field=models.IntegerField(default=-1, max_length=50),
        ),
        migrations.AlterField(
            model_name='crunch',
            name='similarcompany3',
            field=models.IntegerField(default=-1, max_length=50),
        ),
    ]
