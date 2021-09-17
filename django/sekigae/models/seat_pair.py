from core.models import TimestampModelMixin

from django.db import models


class SeatPair(TimestampModelMixin, models.Model):
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    seat_sheet = models.ForeignKey("SeatSheet", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat) + "=" + str(self.student)

    class Meta:
        verbose_name = "seat pair"
        verbose_name_plural = "seat pairs"
