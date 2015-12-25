# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.RemoveField(
            model_name='company',
            name='date_founded',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='numberofEmployees',
        ),
        migrations.RemoveField(
            model_name='company',
            name='total_funding',
        ),
        migrations.AddField(
            model_name='company',
            name='average',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.CharField(default=b'0000000', max_length=200),
        ),
        migrations.AddField(
            model_name='company',
            name='total_Reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(default=b'0000000', max_length=100),
        ),
    ]
