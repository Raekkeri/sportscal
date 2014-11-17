import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from djobjectfactory.factory import ObjectFactory, get_factory
from formsettesthelpers import ModelFormSetHelper

from activities.forms import ActivityFormset


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


class ActivityTypeFactory(ObjectFactory):
    model = 'activities.ActivityType'
    def default(cls, counter, **kwrags):
        return {'name': 'activity type #%d' % counter}


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


class TestCreateView(TestCase):
    def setUp(self):
        self.at1 = ActivityTypeFactory.create()
        self.user = get_factory('auth.User').create(username='raekkeri')
        self.user.set_password('adg')
        self.user.save()

    def test_create_new_view(self):
        self.client.login(username='raekkeri', password='adg')

        fh = ModelFormSetHelper(ActivityFormset)
        data = fh.generate([{'type': self.at1.pk, 'weight': 4}], total_forms=1)
        data['name'] = 'just a jog'
        data['start_time'] = '2014-09-23 12:43'
        data['end_time'] = '2014-09-23 12:43'

        response = self.client.post(reverse('create_activity'), data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(EventFactory.get_model().objects.count(), 1)
        self.assertEquals(ActivityFactory.get_model().objects.get().weight, 4)
