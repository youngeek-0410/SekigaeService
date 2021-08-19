from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from core.models import TimestampModelMixin


class SeatFormat(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

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
