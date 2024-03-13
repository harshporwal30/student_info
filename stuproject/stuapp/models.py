from django.db import models

# Create your models here.

class student(models.Model):
    Gender = (("Male","male"),("Female","female"))
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200,choices=Gender)
    Phoneno = models.BigIntegerField()
    age = models.CharField(max_length=200)

    class Meta:
        db_table = "stuinfo"
    

