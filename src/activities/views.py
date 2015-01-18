from django.http import HttpResponseRedirect
from django.views.generic import View, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from forms import EventForm, ActivityFormset
from models import Event


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class ActivityCreateView(TemplateResponseMixin, LoginRequiredMixin, View):
    template_name = 'activities/create_activity.html'

    def get(self, request, **kwargs):
        return self.render_to_response({
                'event_form': self.get_form(),
                'activity_formset': self.get_activity_formset(None),
                })

    def post(self, request, **kwargs):
        event_form = self.get_form()
        if event_form.is_valid():
            event = event_form.save(commit=False)
            activity_formset = self.get_activity_formset(event)
            if activity_formset.is_valid():
                event.user = self.request.user
                event.save()
                activity_formset.save()
                return HttpResponseRedirect(reverse('list_events'))
        else:
            activity_formset = self.get_activity_formset(None)
        return self.render_to_response({
                'event_form': event_form,
                'activity_formset': activity_formset,
                })

    def get_activity_formset(self, event):
        return ActivityFormset(*self._form_initial(), instance=event)

    def get_form(self):
        return EventForm(*self._form_initial())

    def _form_initial(self):
        if self.request.method == 'POST':
            return [self.request.POST]
        return []


class ModifyActivityView(SingleObjectMixin, ActivityCreateView):
    template_name = 'activities/create_activity.html'
    model = Event

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        return super(ModifyActivityView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        return super(ModifyActivityView, self).post(*args, **kwargs)

    def get_form(self):
        instance = Event.objects.get(
                pk=self.kwargs['pk'], user=self.request.user)
        return EventForm(*self._form_initial(), instance=instance)

    def get_activity_formset(self, event):
        return ActivityFormset(*self._form_initial(), instance=self.object)


class ListActivityView(ListView):
    def get_queryset(self):
        qs = self.request.user.event_set
        qs = qs.order_by('-start_time')
        qs = qs.prefetch_related('activities')
        return qs
