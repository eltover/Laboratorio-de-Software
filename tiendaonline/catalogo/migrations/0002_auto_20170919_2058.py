# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='nombre',
            new_name='nombre_catalogo',
        ),
    ]
