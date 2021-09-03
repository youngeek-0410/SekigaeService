from sekigae.models.seat import Seat
from sekigae.models.seat_sheet import SeatSheet
from sekigae.models.student import Student

from django.db import models


class SeatPair(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    seat_sheet_id = models.ForeignKey(SeatSheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_id

    class Meta:
        verbose_name = "seat_pair"
        verbose_name_plural = "seat_pairs"
