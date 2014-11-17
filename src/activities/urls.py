from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

import views
from models import Event

urlpatterns = patterns('',
    url(r'^new/', views.ActivityCreateView.as_view(), name='create_activity'),
    url(r'^list/',
        login_required(ListView.as_view(
            queryset=Event.objects.prefetch_related('activity_set'))),
        name='list_events'),
)
