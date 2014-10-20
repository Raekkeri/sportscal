from models import Event
from serializers import EventSerializer
from rest_framework import generics, permissions
from permissions import IsOwner


class EventAPIMixin(object):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Event.objects.filter(user=self.request.user)
        else:
            return Event.objects.none()


class EventList(EventAPIMixin, generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsOwner)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetail(EventAPIMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsOwner)
