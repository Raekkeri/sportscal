from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from forms import EventForm, ActivityFormset


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class ActivityCreateView(TemplateResponseMixin, LoginRequiredMixin,View):
    template_name = 'activities/create_activity.html'

    def get(self, request):
        return self.render_to_response({
                'event_form': EventForm(),
                'activity_formset': ActivityFormset(),
                })

    def post(self, request):
        def get_activity_formset(event):
            return ActivityFormset(self.request.POST, instance=event)

        event_form = EventForm(self.request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            activity_formset = get_activity_formset(event)
            if activity_formset.is_valid():
                event.user = self.request.user
                event.save()
                activity_formset.save()
                return HttpResponseRedirect(reverse('list_events'))
        else:
            activity_formset = get_activity_formset(None)
        return self.render_to_response({
                'event_form': event_form,
                'activity_formset': activity_formset,
                })
