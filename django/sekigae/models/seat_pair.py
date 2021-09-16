from core.models import TimestampModelMixin
from sekigae.models.seat import Seat
from sekigae.models.seat_sheet import SeatSheet
from sekigae.models.student import Student

from django.db import models


class SeatPair(TimestampModelMixin, models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    seat_sheet = models.ForeignKey(SeatSheet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat) + "&" + str(self.student)

    class Meta:
        verbose_name = "seat_pair"
        verbose_name_plural = "seat_pairs"
