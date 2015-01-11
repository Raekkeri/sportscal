# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytype',
            name='distance_multiplier',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitytype',
            name='duration_multiplier',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitytype',
            name='repititions_multiplier',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitytype',
            name='weight_multiplier',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(related_name=b'activities', to='activities.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
