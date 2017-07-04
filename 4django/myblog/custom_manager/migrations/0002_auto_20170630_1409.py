# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-30 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('custom_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=225)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
        migrations.AlterModelManagers(
            name='todo',
            managers=[
                ('todolist', django.db.models.manager.Manager()),
            ],
        ),
    ]