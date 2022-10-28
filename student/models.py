from statistics import mode
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_first_name(value) : 
    if value[0] < 'a' or value[0] > 'z' :
        raise ValidationError(_("%(value)s must not start with small letter"), params={'value':value})
class Parent (models.Model) : 
    first_name = models.CharField(max_length = 70 , validators = [validate_first_name])
    last_name = models.CharField(max_length = 70)
    age = models.IntegerField()
    email = models.EmailField(max_length=100 , blank=True , null=True)
    password = models.CharField(max_length = 50  , blank=True , null=True)
    def __str__(self) : 
        return self.email
    
    class Meta : 
        db_table = "Parents" 


class Student (models.Model) : 
    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 70)
    email = models.CharField(max_length = 70) 
    age = models.IntegerField() 
    class_name = models.CharField(max_length = 50) 
    parent = models.ForeignKey(Parent , related_name = "children" , on_delete = models.CASCADE , blank=True , null=True )
    email = models.EmailField(max_length=100  , blank=True , null=True)
    password = models.CharField(max_length = 50 , blank=True , null=True)
    def __str__(self) : 
        return self.first_name + " " + self.last_name 
    
    class Meta : 
        db_table = "Students" 
        constraints=[
			models.CheckConstraint(name='not starts with m', check=~models.Q(first_name__startswith="m"))
		]
      



class Subject(models.Model) : 
    name =  models.CharField(max_length=70) 
    students = models.ManyToManyField(Student , related_name = "subjects")
    def __str__(self) : 
        return self.name 
    
    class Meta : 
        db_table = "Subjects" 
       

class ParentActiveUsers (models.Model) :
    authenticationKey = models.CharField(max_length = 300) 
    user = models.ForeignKey(Parent , related_name = "activeUsers" , on_delete = models.CASCADE , null = True)

    class Meta : 
        db_table = "ParentActiveUsers" 

class StudentActiveUsers (models.Model) :
    authenticationKey = models.CharField(max_length = 300) 
    user = models.ForeignKey(Student , related_name = "activeUsers" , on_delete = models.CASCADE ,  null = True)

    class Meta : 
        db_table = "StudentActiveUsers" 


