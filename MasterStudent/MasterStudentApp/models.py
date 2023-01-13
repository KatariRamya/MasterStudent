from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Master(models.Model):
    Master_Name=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=30)
    Email=models.CharField(max_length=40)
    Password=models.CharField(max_length=40)

class Student(models.Model):
    Student_Name = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=50)
    Email = models.CharField(max_length=40)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.Student_Name}'


class Task(models.Model):
    Left=models.CharField(max_length=20)
    Operation=models.CharField(max_length=10)
    Right=models.CharField(max_length=10)
    Students=models.ForeignKey(Student,on_delete=CASCADE)
    Status=models.BooleanField(default=False)


