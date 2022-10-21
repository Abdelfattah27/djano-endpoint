from ast import Delete
import email
from django.shortcuts import HttpResponse, render 
import json
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from .models import Student

class CRUDStudents(View) : 
    def get(self , request ) : 
        try :
            students =json.loads(serializers.serialize("json" , Student.objects.filter()))
            return JsonResponse(students , safe=False)
        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
    def post(self , request)  :
        try : 
            for i in json.loads(request.body) : 
                Student.objects.create(first_name = i["first_name"] , last_name = i["last_name"] , email = i["email"] , age = i["age"] , class_name = i["class_name"])
            return JsonResponse({"status " : "Added Successfully"})
        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
            
class CRUDStudent(View) : 
    def get(self , request , id) : 
        try : 
            student = Student.objects.get(id = id) 
            serialized_student = serializers.serialize("json" , [student , ])
            return JsonResponse(json.loads(serialized_student) , safe=False)
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def put(self , request , id) : 
        try : 
            updated_student = json.loads(request.body)
            student = Student.objects.filter(id = id).update(first_name = updated_student["first_name"] , last_name = updated_student["last_name"] , email = updated_student["email"] , age = updated_student["age"] , class_name =updated_student["class_name"])
            return JsonResponse({"status" : "updated successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def delete(self , request , id) : 
        try : 
            Student.objects.get(id = id).delete() 
            return JsonResponse({"status" : "Deleted Successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
     