# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_auto_20190505_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangmodel',
            name='gambar',
            field=models.ImageField(default='default_barang.jpg', upload_to='profile_pics'),
        ),
    ]