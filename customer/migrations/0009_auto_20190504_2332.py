# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20190504_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangmodel',
            name='gambar',
            field=models.ImageField(upload_to='profile_pics/'),
        ),
    ]
