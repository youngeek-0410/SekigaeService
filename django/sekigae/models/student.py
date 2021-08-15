from django.db import models
from sekigae.models.student_sheet import StudentSheet

class Student(models.Model):
	name = models.CharField(max_length=255)
	number = models.PositiveSmallIntegerField()
	student_sheet_id = models.ForeignKey(StudentSheet, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "student"
		verbose_name_plural = "students"

