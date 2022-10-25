from django.shortcuts import render 
import json
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from .models import Student , Parent , Subject
from .forms import StudentForm

def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

class CRUDStudents(View) : 
    def get(self , request ):
        try :
            students =json.loads(serializers.serialize("json" , Student.objects.filter()))
            return JsonResponse(students , safe=False)

        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
    def post(self , request)  :
        try :
            students = json.loads(request.body)  
            if type(students) is not list :
                students = [students , ]
            for student in students : 
                form = StudentForm(data = student )
                if form.is_valid() :
                    form.save() 
                else : 
                    return JsonResponse({"Errors" : form.errors} , status = 500)
                new_student = Student.objects.create(**without_keys(student , "parent"))
                if "parent" in student : 
                    parent = Parent.objects.get(id = student["parent"])
                    new_student.parent = parent
                    new_student.save() 
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
            Student.objects.filter(id = id).update(**without_keys(updated_student, "parent"))
            new_student =  Student.objects.get(id = id)
            if "parent" in updated_student : 
                print("passed this")
                parent = Parent.objects.get(id = updated_student["parent"])
                new_student.parent = parent
                new_student.save() 
            return JsonResponse({"status" : "updated successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def delete(self , request , id) : 
        try : 
            Student.objects.get(id = id).delete() 
            return JsonResponse({"status" : "Deleted Successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})



class CRUDParents(View) : 
    def get(self , request ) : 
        try :
            parents =json.loads(serializers.serialize("json" , Parent.objects.filter()))
            return JsonResponse(parents , safe=False)
        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
    def post(self , request)  :
        try :
            parents =  json.loads(request.body)
            if type(parents) is not list : 
                parents = [parents , ]
            for i in parents : 
                Parent.objects.create(**i)
            return JsonResponse({"status " : "Added Successfully"})
        except Exception as ex : 
            return JsonResponse({"status" : str(type(ex))})
            
class CRUDParent(View) : 
    def get(self , request , id) : 
        try : 
            parent = Parent.objects.get(id = id) 
            serialized_parent = serializers.serialize("json" , [parent , ])
            return JsonResponse(json.loads(serialized_parent) , safe=False)
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def put(self , request , id) : 
        try : 
            Parent.objects.filter(id = id).update(**json.loads(request.body))
            return JsonResponse({"status" : "updated successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def delete(self , request , id) : 
        try : 
            Parent.objects.get(id = id).delete() 
            return JsonResponse({"status" : "Deleted Successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})




class CRUDSubjects(View) : 
    def get(self , request ) : 
        try :
            subjects =json.loads(serializers.serialize("json" , Subject.objects.filter()))
            return JsonResponse(subjects , safe=False)

        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
    def post(self , request)  :
        try :
            new_subjects =  json.loads(request.body) 
            if type(new_subjects) is not list :
                new_subjects = [new_subjects , ]
            for subject_i in new_subjects :  
                added_subject = Subject.objects.create(name = subject_i["name"])
                if "student" in subject_i  :
                    students = subject_i["student"]
                    if type(students) is list : 
                        for student in students : 
                            added_subject.students.add(student)
                    else : 
                        added_subject.students.add(students)
            return JsonResponse({"status " : "Added Successfully"})
        except Exception as ex : 
            return JsonResponse({"status" : str(ex)})
            
class CRUDSubject(View) : 
    def get(self , request , id) : 
        try : 
            subject = Subject.objects.get(id = id) 
            serialized_subject = serializers.serialize("json" , [subject , ])
            return JsonResponse(json.loads(serialized_subject) , safe=False)
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def put(self , request , id) : 
        try : 
            old_subject = Subject.objects.get(id = id)
            updated_subject = json.loads(request.body) ; 
            setattr(old_subject , "name" , updated_subject["name"])
            if type(updated_subject["students"]) is list : 
                for student in updated_subject["students"] : 
                    print(student)
                    old_subject.students.add(student)
            else : 
                old_subject.students.add(updated_subject["students"])
            old_subject.save()
            return JsonResponse({"status" : "updated successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})
    def delete(self , request , id) : 
        try : 
            Subject.objects.get(id = id).delete() 
            return JsonResponse({"status" : "Deleted Successfully"})
        except Exception as ex  : 
            return JsonResponse({"status" : str(ex)})

