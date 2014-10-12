from django import forms
from django.forms.models import inlineformset_factory

import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ('start_time', 'end_time')


ActivityFormset = inlineformset_factory(models.Event, models.Activity,
        fields=('type', 'event', 'distance', 'duration', 'weight',
            'repetitions'))
