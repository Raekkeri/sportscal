from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext as _

from scores import AVAILABLE_SCORES


class Event(models.Model):
    user = models.ForeignKey('auth.User')
    start_time = models.DateTimeField(_('Start time'))
    end_time = models.DateTimeField(_('End time'))
    name = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-start_time']

    def get_score(self):
        return sum(o.get_score() for o in self.activities.all())


multiplier_kwargs = dict(
        max_digits=8,
        decimal_places=2,
        default=Decimal('0.00'),
        )

class ActivityType(models.Model):
    name = models.CharField(_('Name'), max_length=256)
    description = models.TextField(_('Description'), default='')
    distance_multiplier = models.DecimalField(**multiplier_kwargs)
    duration_multiplier = models.DecimalField(**multiplier_kwargs)
    weight_multiplier = models.DecimalField(**multiplier_kwargs)
    repititions_multiplier = models.DecimalField(**multiplier_kwargs)
    scorer = models.CharField(max_length=256, default='', blank=True,
            choices=[(k, k) for k in AVAILABLE_SCORES.iterkeys()])

    def __unicode__(self):
        return self.name

    def get_scorer(self):
        return AVAILABLE_SCORES.get(self.scorer, None)


class Activity(models.Model):
    type = models.ForeignKey(ActivityType)
    event = models.ForeignKey(Event, related_name='activities')
    distance = models.PositiveIntegerField(_('Distance'), default=0)
    duration = models.PositiveIntegerField(_('Duration'), default=0)
    weight = models.IntegerField(_('Weight'), default=0)
    repetitions = models.PositiveIntegerField(_('Repetitions'), default=0)

    def get_score(self):
        scorer = self.type.get_scorer()
        if scorer:
            return scorer.get_score(self)
        else:
            return 0

    def get_duration(self):
        start, end = self.event.start_time, self.event.end_time
        if self.duration:
            return self.duration
        elif start and end and start < end:
            return (end - start).seconds
        return 0
