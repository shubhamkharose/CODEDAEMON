# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leader', '0041_cont_1_sub_cont_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='cont_1',
            name='Magical_String',
            field=models.IntegerField(default=0),
        ),
    ]