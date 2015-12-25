# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0011_crunch_extra_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='crunch',
            name='similarcompany1',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='crunch',
            name='similarcompany2',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='crunch',
            name='similarcompany3',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
