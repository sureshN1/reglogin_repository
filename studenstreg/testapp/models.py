from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    sid=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.IntegerField()