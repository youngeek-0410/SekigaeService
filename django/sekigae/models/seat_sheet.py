from core.models import TimestampModelMixin
from sekigae.models.student_sheet import StudentSheet
from sekigae.models.user import User

from django.db import models


class SeatSheet(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    student_sheet = models.ForeignKey(StudentSheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "seat_sheet"
        verbose_name_plural = "seat_sheets"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "user_id"],
                name="seat_sheet_unique",
            ),
        ]
