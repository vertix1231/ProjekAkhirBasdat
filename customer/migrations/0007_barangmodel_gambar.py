# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20190502_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangmodel',
            name='gambar',
            field=models.FileField(blank=True, null=True, upload_to='gambar/'),
        ),
    ]
