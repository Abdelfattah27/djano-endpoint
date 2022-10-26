from django import forms
from .models import Student
from django.forms import ValidationError

def check_first_name(value):
	if value[0] == 'm':
		raise ValidationError('m is forbidden')
def check_age(value) : 
    if value < 0 or value > 100 : 
        raise ValidationError('age must be between 0 to 100')

class StudentForm(forms.ModelForm):
	age = forms.IntegerField(required=False, validators=[check_age]) 
	first_name = forms.CharField(max_length=100, validators=[check_first_name])
	class Meta:
		model = Student
		fields = "__all__"