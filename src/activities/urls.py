from django.conf.urls import patterns, url
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required

import views, api_views
from models import Event

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='activities/base.html'),
        name='frontpage'),
    url(r'^new/', views.ActivityCreateView.as_view(), name='create_activity'),
    url(r'^modify/(?P<pk>\d+)/$', views.ModifyActivityView.as_view(),
        name='modify_activity'),
    url(r'^list/',
        login_required(ListView.as_view(
            queryset=Event.objects.order_by(
                '-start_time').prefetch_related('activities'))),
        name='list_events'),
    url(r'^events/$', api_views.EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', api_views.EventDetail.as_view()),
)
