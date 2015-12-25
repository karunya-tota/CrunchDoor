# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0009_auto_20151204_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='crunch',
            name='crunch_id',
            field=models.ForeignKey(null=True, db_column=b'company_id', to='crunchDoorApp.Company', unique=True),
        ),
    ]
