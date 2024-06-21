from django.db import models
from django.utils import timezone

class Student(models.Model):
    username = models.CharField(max_length=50, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telegram_id = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)

class Student_courses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

class Section(models.Model):
    name = models.CharField(max_length=50)
    themes = models.TextField(default=None)


class Section_themes(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


