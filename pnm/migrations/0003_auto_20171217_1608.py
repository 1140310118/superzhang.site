# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnm', '0002_auto_20171216_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
