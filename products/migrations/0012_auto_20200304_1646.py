# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200304_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentperfume',
            name='score',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]
