from django.db import models
from account.models import User
from django.utils import timezone


class StudentSheet(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "student_sheet"
		verbose_name_plural = "student_sheets"

