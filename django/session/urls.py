from django.urls import path
from . import views

app_name = 'session'

urlpatterns = [
    path('temp-index', views.TempIndexView.as_view(), name='temp_index'),
    path('signin', views.SigninView.as_view(), name='signin'),
    path('signin-callback', views.signin_callback, name='signin_callback'),
    path('signout', views.signout, name="signout"),
]
