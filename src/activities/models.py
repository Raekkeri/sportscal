from django.db import models
from django.utils.translation import ugettext as _



class Event(models.Model):
    user = models.ForeignKey('auth.User')
    start_time = models.DateTimeField(_('Start time'))
    end_time = models.DateTimeField(_('End time'))


class ActivityType(models.Model):
    name = models.CharField(_('Name'), max_length=256)
    description = models.TextField(_('Description'), default='')


class Activity(models.Model):
    type = models.ForeignKey(ActivityType)
    event = models.ForeignKey(Event)
    distance = models.PositiveIntegerField(_('Distance'), default=0)
    duration = models.PositiveIntegerField(_('Duration'), default=0)
    weight = models.IntegerField(_('Weight'), default=0)
    repetitions = models.PositiveIntegerField(_('Repetitions'), default=0)
