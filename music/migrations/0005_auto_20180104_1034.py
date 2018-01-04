# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Desp',
            new_name='desp',
        ),
    ]
