# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20150110_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytype',
            name='scorer',
            field=models.CharField(default=b'', max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
