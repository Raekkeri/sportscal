from django.views.generic import ListView


class GroupListView(ListView):
    def get_queryset(self):
        return self.request.user.group_set.all()
