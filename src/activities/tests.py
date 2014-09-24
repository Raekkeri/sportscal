import datetime

from django.test import TestCase
from djobjectfactory.factory import ObjectFactory, get_factory


class EventFactory(ObjectFactory):
    model = 'activities.Event'

    def default(cls, counter, **kwargs):
        ret = {
            'start_time': datetime.datetime.now(),
            'end_time': datetime.datetime.now() + datetime.timedelta(hours=1),
            }
        if 'user' not in kwargs:
            ret['user'] = get_factory('auth.User').create()
        return ret


EventFactory = get_factory('activities.Event')
ActivityTypeFactory = get_factory('activities.ActivityType')
ActivityFactory = get_factory('activities.Activity')


class TestActivity(TestCase):
    def test_create_simple_activity(self):
        running = ActivityTypeFactory.create(name='Running')
        stretching = ActivityTypeFactory.create(name='Stretching')
        workout = EventFactory.create()
        workout.activity_set.create(
            type=running, distance=12000, duration=70 * 60)
        workout.activity_set.create(type=stretching, duration=10 * 60)
        self.assertEquals(ActivityFactory.get_model().objects.count(), 2)
