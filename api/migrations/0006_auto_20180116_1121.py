# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180116_1116'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=set([]),
        ),
    ]