import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from djobjectfactory.factory import ObjectFactory, get_factory
from formsettesthelpers import ModelFormSetHelper

from activities.forms import ActivityFormset
from activities.models import Event


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
        workout.activities.create(
            type=running, distance=12000, duration=70 * 60)
        workout.activities.create(type=stretching, duration=10 * 60)
        self.assertEquals(ActivityFactory.get_model().objects.count(), 2)


class BaseTestCase(TestCase):
    def setUp(self):
        self.at1 = ActivityTypeFactory.create()
        self.user = get_factory('auth.User').create(username='raekkeri')
        self.user.set_password('adg')
        self.user.save()
        self.client.login(username='raekkeri', password='adg')


class TestCreateView(BaseTestCase):
    def test_create_new_view(self):
        fh = ModelFormSetHelper(ActivityFormset)
        data = fh.generate([{'type': self.at1.pk, 'weight': 4}], total_forms=1)
        data['name'] = 'just a jog'
        data['start_time'] = '2014-09-23 12:43'
        data['end_time'] = '2014-09-23 12:43'

        response = self.client.post(reverse('create_activity'), data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(EventFactory.get_model().objects.count(), 1)
        self.assertEquals(ActivityFactory.get_model().objects.get().weight, 4)


class TestModifyView(BaseTestCase):
    def test_modify_dates(self):
        self.event = EventFactory.create(user=self.user)
        fh = ModelFormSetHelper(ActivityFormset)
        data = fh.generate([], total_forms=0)
        data['name'] = 'swim'
        data['start_time'] = '2014-09-23 12:43'
        data['end_time'] = '2014-09-23 12:43'
        response = self.client.post(
                reverse('modify_activity', args=[self.event.pk]), data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Event.objects.count(), 1)
        obj = Event.objects.get()
        self.assertEquals(obj.name, 'swim')
        self.assertEquals(obj.start_time.year, 2014)
        self.assertEquals(obj.start_time.month, 9)

    def test_modify_activities(self):
        self.event = EventFactory.create(user=self.user)
        at = ActivityTypeFactory.create(name='running')
        at2 = ActivityTypeFactory.create(name='swimming')
        a1 = ActivityFactory.create(type=at, event=self.event, distance=2)
        fh = ModelFormSetHelper(ActivityFormset)
        data = fh.generate([
            {'id': a1.id, 'type': at2.id, 'distance': 3}], total_forms=1,
            initial_forms=1)
        data['name'] = 'swim'
        data['start_time'] = '2014-09-23 12:43'
        data['end_time'] = '2014-09-23 12:43'
        response = self.client.post(
                reverse('modify_activity', args=[self.event.pk]), data)
        obj = Event.objects.get()
        activity = obj.activities.get()
        self.assertEquals(activity.type, at2)
        self.assertEquals(activity.distance, 3)
