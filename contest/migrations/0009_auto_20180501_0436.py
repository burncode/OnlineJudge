# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-01 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_contest_allowed_ip_ranges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='password',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='rule_type',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contest',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contestannouncement',
            name='title',
            field=models.TextField(),
        ),
    ]