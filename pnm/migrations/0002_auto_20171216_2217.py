# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, to='pnm.Catalog'),
        ),
    ]
