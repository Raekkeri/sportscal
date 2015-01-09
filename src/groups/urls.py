from django.conf.urls import patterns, url
from views import GroupListView


urlpatterns = patterns('',
    url(r'^my-groups/$', GroupListView.as_view()),
)
