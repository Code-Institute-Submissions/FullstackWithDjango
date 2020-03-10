# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-10 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20200310_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('street_address', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Perfume')),
            ],
        ),
    ]
