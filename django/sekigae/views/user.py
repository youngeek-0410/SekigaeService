from django.views.generic import TemplateView, DeleteView
from ..account.models import User
from django import http


class UserGetView(TemplateView):
    template_name = 'account/base_account.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['account'] = user
        return context


class UserDeleteView(DeleteView):
    model = User
    success_url = '/path/to/success/url'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.User == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return http.HttpResponceRedirect(success_url)
        else:
            return http.HttpResponceForbidden("cannot delete")
