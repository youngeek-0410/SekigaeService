from django.contrib import admin

from .models.seat_format import SeatFormat
from .models.seat import Seat
from .models.student import Student
from .models.student_sheet import StudentSheet

# Register your models here.
admin.site.register(Seat)
admin.site.register(SeatFormat)
admin.site.register(Student)
admin.site.register(StudentSheet)
