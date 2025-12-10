from django.db import models

# Create your models here.
class student(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    dept=models.CharField(max_length=100)
    ph=models.CharField(max_length=10)