# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'resume',
            },
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
