# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171212_1428'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=set([]),
        ),
    ]
