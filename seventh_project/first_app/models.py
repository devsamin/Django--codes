from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=29)
    address = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return f"name : {self.name}"