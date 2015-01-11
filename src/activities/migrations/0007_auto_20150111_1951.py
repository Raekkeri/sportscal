# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20150111_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='scorer',
            field=models.CharField(default=b'', max_length=256, blank=True, choices=[(b'BaseScore', b'BaseScore'), (b'DistanceBasedScore', b'DistanceBasedScore'), (b'DurationBasedScore', b'DurationBasedScore')]),
        ),
    ]
