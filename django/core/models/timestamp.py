from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampModelMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated_at"),
        auto_now=True,
    )
