from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

User = get_user_model()


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "account/base_account.html"
    model = User

    # ! post -> delete (templateを使用するときはdelete methodが使えない)
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        logout(request)
        user.delete()
        # TODO: consider redirect page
        return render(request, "sekigae/top.html")
