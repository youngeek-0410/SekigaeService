from django.urls import path
from . import views
from .views import IndexView
from .views import DashboardView

app_name = 'sekigae'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]
