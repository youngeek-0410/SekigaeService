from django.contrib import admin

# Register your models here.

from .models.student import Student
from .models.student_sheet import StudentSheet

admin.site.register(Student)
admin.site.register(StudentSheet)
