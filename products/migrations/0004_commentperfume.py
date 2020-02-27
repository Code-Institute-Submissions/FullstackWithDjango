# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-27 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200226_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPerfume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('score', models.IntegerField(verbose_name=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='products.Perfume')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]