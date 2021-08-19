from django.urls import path
from . import views
from .views import IndexView, student_sheets, student_sheets_detail, student_sheets_test, student_sheets_detail_test

app_name = 'sekigae'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student_sheets', student_sheets, name='student_sheet'),
    path('student_sheets/<int:pk>', student_sheets_detail, name='student_sheets_detail'),
    path('student_sheets_test', student_sheets_test, name='student_sheets_test'),
    path('student_sheets_detail_test/', student_sheets_detail_test, name='student_sheets_detail_test')
]
