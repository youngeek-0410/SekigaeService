from django.db import models
from account.models import User
from django.utils import timezone
from core.models import TimestampModelMixin


class SeatFormat(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "owner"],
                name="unique_sheet_format"
            )
        ]
        verbose_name = "seat format"
        verbose_name_plural = "seat formats"
