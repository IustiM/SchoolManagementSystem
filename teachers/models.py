from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=255)
    subject = models.CharField(max_length=100, default="")
    office = models.CharField(max_length=20, default="")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.teacher} - {self.day_of_week}"


class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher} - {self.date}"
