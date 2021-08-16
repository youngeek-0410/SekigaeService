from django.db import models
from account.models import User
from django.utils import timezone


class SeatFormat(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
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
