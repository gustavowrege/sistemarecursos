# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-21 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemarecursos', '0003_auto_20180119_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='recurso',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='etapaRecurso',
        ),
        migrations.AddField(
            model_name='candidato',
            name='etapaRecurso',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistemarecursos.EtapaRecurso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recurso',
            name='candidato',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='sistemarecursos.Candidato'),
            preserve_default=False,
        ),
    ]
