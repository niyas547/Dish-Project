from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Dishes(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.PositiveBigIntegerField()
    rating=models.FloatField(default=3)
