from django.db import models
from .seat_format import SeatFormat

class Seat(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    seat_format = models.ForeignKey(SeatFormat, on_delete=models.CASCADE)

    def __str__(self):
        return "{}[{}][{}]".format(self.seat_format.name, self.row, self.column)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["row", "column", "seat_format"],
                name="unique_row_column"
            )
        ]

        verbose_name = "seat"
        verbose_name_plural = "seats"