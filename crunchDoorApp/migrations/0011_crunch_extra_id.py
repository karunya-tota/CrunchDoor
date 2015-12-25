# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0010_crunch_crunch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='crunch',
            name='extra_id',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
