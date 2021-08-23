from django.urls import path
from . import views
from .views import IndexView, student_sheets_test, student_sheets_detail_test, StudentSheetsView, StudentSheetDetailView

app_name = 'sekigae'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student_sheets', StudentSheetsView.as_view(), name='student_sheet'),
    path('student_sheets/<int:pk>', StudentSheetDetailView.as_view(), name='student_sheets_detail'),
    path('student_sheets_test', student_sheets_test, name='student_sheets_test'),
    path('student_sheets_detail_test/', student_sheets_detail_test, name='student_sheets_detail_test')
]
