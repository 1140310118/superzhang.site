# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnm', '0003_auto_20171217_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='pid',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='paper_id',
            new_name='paper',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='pid',
            new_name='catalog',
        ),
    ]
