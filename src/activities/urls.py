from django.conf.urls import patterns, url
from django.views.generic import ListView

import views
from models import Event

urlpatterns = patterns('',
    url(r'^new/', views.ActivityCreateView.as_view(), name='create_activity'),
    url(r'^list/',
        ListView.as_view(
            queryset=Event.objects.prefetch_related('activity_set')),
        name='list_events'),
)
