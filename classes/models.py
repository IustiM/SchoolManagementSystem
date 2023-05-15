from django.db import models
from django.utils import timezone

from students.models import Student
from teachers.models import Teacher


class Class(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10,
                                   choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                            ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                                            ('Sunday', 'Sunday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day_of_week} - {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {self.class_obj.name}"
