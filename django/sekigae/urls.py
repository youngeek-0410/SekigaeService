from django.urls import path
from . import views
from .views import IndexView, user

app_name = 'sekigae'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user', user.UserView.as_view(), name='user'),
	path('user', user.UserView.as_view(), name='user_delete')
]
