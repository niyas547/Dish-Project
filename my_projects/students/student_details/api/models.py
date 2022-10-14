from django.db import models


# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=120)
    roll_number=models.CharField(max_length=120)
    age=models.CharField(max_length=120)
    phone=models.PositiveIntegerField()
    place=models.CharField(max_length=120)

