# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogspost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='addition_control_msg',
            field=models.CharField(max_length=150, default='0000000000'),
        ),
    ]
