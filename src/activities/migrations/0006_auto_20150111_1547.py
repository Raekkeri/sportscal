# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_activitytype_scorer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='scorer',
            field=models.CharField(default=b'', max_length=256, blank=True, choices=[(b'BaseScore', b'BaseScore'), (b'DistanceBasedScore', b'DistanceBasedScore')]),
        ),
    ]
