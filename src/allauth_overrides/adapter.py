from django.core.urlresolvers import reverse
from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('frontpage')
