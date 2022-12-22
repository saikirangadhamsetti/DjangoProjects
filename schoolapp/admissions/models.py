from django.db import models
from django.urls import reverse
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=10)
    phn=models.CharField(max_length=10)
    clas=models.IntegerField(default="10")

class Teacher(models.Model):
    name=models.CharField(max_length=10)
    exp=models.IntegerField()
    subject=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    def get_absolute_url(self):
        return reverse("listteachers")