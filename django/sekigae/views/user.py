from django.views.generic import TemplateView, DeleteView
from ..account.models import User
from django import http

class UserView(TemplateView):
	template_name = 'account/base_account.html'
	def get(self, request, *arg, **kwargs):
		user = self.request.user
		context = {'account': user}
		return self.render_to_response(context)


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
