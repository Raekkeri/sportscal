# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20141012_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
