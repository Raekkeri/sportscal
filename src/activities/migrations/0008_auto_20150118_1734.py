# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20150111_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_time']},
        ),
        migrations.RenameField(
            model_name='activitytype',
            old_name='repititions_multiplier',
            new_name='repetitions_multiplier',
        ),
    ]
