from statistics import mode
from django.db import models

# Create your models here.

class Student (models.Model) : 
    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 70)
    email = models.CharField(max_length = 70) 
    age = models.IntegerField() 
    class_name = models.CharField(max_length = 50) 

    def __str__(self) : 
        return self.first_name + " " + self.last_name 
    
    class Meta : 
        db_table = "Students" 