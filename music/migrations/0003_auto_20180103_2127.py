# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180103_2123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Post',
        ),
    ]
