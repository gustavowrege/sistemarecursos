# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemarecursos', '0005_auto_20180126_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
