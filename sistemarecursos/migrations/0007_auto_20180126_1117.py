# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 13:17
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemarecursos', '0006_candidato_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='textoRecurso',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
