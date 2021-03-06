# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20171220_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='fav_by',
            field=models.ManyToManyField(related_name='favorites', to='quotes.User'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotes.User'),
        ),
    ]
