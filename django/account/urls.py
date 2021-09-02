from django.urls import path

from .views import UserView

app_name = "account"

urlpatterns = [
    path("user", UserView.as_view(), name="user"),
]
