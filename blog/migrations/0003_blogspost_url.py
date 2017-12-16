# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogspost_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='url',
            field=models.CharField(max_length=150, default='11'),
        ),
    ]
