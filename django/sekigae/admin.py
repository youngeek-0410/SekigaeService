from django.contrib import admin

from .models.seat_format import SeatFormat
from .models.seat import Seat

# Register your models here.
admin.site.register(Seat)
admin.site.register(SeatFormat)
