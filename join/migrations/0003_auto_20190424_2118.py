# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-24 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0002_auto_20190423_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='first_name',
            new_name='name',
        ),
    ]