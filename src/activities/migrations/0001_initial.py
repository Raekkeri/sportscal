# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.PositiveIntegerField(default=0, verbose_name='Distance')),
                ('duration', models.PositiveIntegerField(default=0, verbose_name='Duration')),
                ('weight', models.IntegerField(default=0, verbose_name='Weight')),
                ('repetitions', models.PositiveIntegerField(default=0, verbose_name='Repetitions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(default=b'', verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(to='activities.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(to='activities.ActivityType'),
            preserve_default=True,
        ),
    ]
