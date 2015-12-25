# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0004_crunch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crunch',
            old_name='employes',
            new_name='employees',
        ),
    ]
