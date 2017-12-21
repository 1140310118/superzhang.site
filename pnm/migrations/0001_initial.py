# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('pid', models.ForeignKey(to='pnm.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('paper_type', models.CharField(max_length=2)),
                ('url', models.CharField(max_length=150, default='')),
                ('pid', models.ForeignKey(to='pnm.Catalog')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='paper_id',
            field=models.ForeignKey(to='pnm.Paper'),
        ),
    ]
