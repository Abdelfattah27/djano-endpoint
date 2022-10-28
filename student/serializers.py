from rest_framework import serializers
from .models import Parent, Student , Subject
from django.forms import ValidationError

def validate_first_name(value) : 
    if value[0] == 'M' : 
        raise ValidationError("FirstName must start with uppercase letter")


def check_age(value) : 
    if value < 0 or value > 100 : 
        raise ValidationError("Age must be positive number smaller than 100 ")
class LoginSerializer(serializers.ModelSerializer) : 
    email = serializers.EmailField(max_length=100 )
    password = serializers.CharField(max_length = 50 )
    class Meta : 
        model = Parent
        fields = ['email' , 'password']
class ParentSerializer(serializers.ModelSerializer) :
    first_name = serializers.CharField(max_length = 70 , validators = [validate_first_name])
    last_name = serializers.CharField(max_length = 70)
    age = serializers.IntegerField(validators = [check_age])
    email = serializers.EmailField(max_length=100 )
    password = serializers.CharField(max_length = 50 )
    class Meta : 
        model = Parent
        fields = ['age' , 'first_name' , 'last_name' , 'email' , 'password']



class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 70)
    last_name = serializers.CharField(max_length = 70)
    email = serializers.CharField(max_length = 70) 
    age = serializers.IntegerField(validators = [check_age]) 
    class_name = serializers.CharField(max_length = 50) 
    password = serializers.CharField(max_length = 50 )

    class Meta : 
        model = Student 
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer) :
    name = serializers.CharField(max_length = 70)
    class Meta : 
        model = Subject
        fields = '__all__'