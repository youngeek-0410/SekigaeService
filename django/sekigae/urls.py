from django.urls import path
from . import views
from .views import index

app_name = 'sekigae'

urlpatterns = [
  path('', index.index, name='index'),
]
