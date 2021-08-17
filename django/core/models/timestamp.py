from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampModelMixin(models.Model):
    class Meta:
        abstract = True

    create_at = models.DateTimeField(
        verbose_name=_("create_at"),
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_("update_at"),
        auto_now=True,
    )
