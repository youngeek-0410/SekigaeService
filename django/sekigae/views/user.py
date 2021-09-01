from django.views.generic import TemplateView
from account.models import User
from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'account/base_account.html'
    model = User

# def __init__(self, *args, **kwargs):	
# model = User

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['account'] = user
        return context

    def get_success_url(self):
        return reverse('sekigae:user')

    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        request.user.delete()
        return http.HttpResponseRedirect(success_url)
