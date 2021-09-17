from core.models import TimestampModelMixin

from django.contrib.auth import get_user_model
from django.db import models


class SeatSheet(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    student_sheet = models.ForeignKey("StudentSheet", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "seat sheet"
        verbose_name_plural = "seat sheets"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "owner_id"],
                name="seat_sheet_unique",
            ),
        ]
