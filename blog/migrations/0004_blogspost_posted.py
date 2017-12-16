# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogspost_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='posted',
            field=models.BooleanField(default=True),
        ),
    ]
