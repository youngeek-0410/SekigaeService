from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from core.models import TimestampModelMixin


class StudentSheet(TimestampModelMixin, models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "student sheet"
        verbose_name_plural = "student sheets"
