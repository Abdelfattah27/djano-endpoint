from django.shortcuts import render 
from .models import Student , Parent, StudentActiveUsers , ParentActiveUsers
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins , generics
from .serializers import ParentSerializer, StudentSerializer , LoginSerializer
from .middlewares import ParentAuthentication, ParentDataPermissions, RegisterAuthentication ,StudentAuthentication , StudentDataPermissions , ListOfDataAuthentication
import json
import jwt
from datetime import datetime
from django.core import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ParentLogin(generics.GenericAPIView) : 
    
    queryset = Parent.objects.all()
    serializer_class = LoginSerializer
    @swagger_auto_schema(
	operation_summary='Login as parent',
	operation_description="""
	**send request with email and password**
	you will get authentication key that will used in header of any coming request use header name as **Authorization** """, 
	responses={400:'not-found',
	403: 'unprocessable entity'},
	)
    def post(self, request, *args, **kwargs):
        try : 
            user = Parent.objects.filter(Q(email=request.data["email"])&Q(password=request.data["password"])) 
            if len(user) > 0 : 
                now = datetime.now().strftime("%d/%m/%Y%H:%M:%S")
                request.data["dateTime"] = now 
                encoded_jwt = jwt.encode(request.data , "secret", algorithm="HS256")
                ParentActiveUsers.objects.create(authenticationKey = encoded_jwt , user = user[0] )
                return Response({"your authentication key is save it" : encoded_jwt})

            else : 
                return Response({"Message" : "Wrong password or email"}) 
        except Exception as ex : 
            return Response({"Message" : str(ex)})
 
        
class ParentRegister(generics.GenericAPIView, mixins.CreateModelMixin ) :
    authentication_classes = [RegisterAuthentication]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    @swagger_auto_schema(
	operation_summary='Register as parent',
	operation_description="""
	**send request with parent data**
	that will create a new parent ad store it in the database """, 
	responses={400:'not-found',
	403: 'unprocessable entity'},
	)
    def post(self, request, *args, **kwargs):
        try : 
            return self.create(request, *args, **kwargs)
        except Exception as ex : 
            return Response({"Message" : str(ex)})

class ParentDetailView(generics.DestroyAPIView,generics.UpdateAPIView,generics.RetrieveAPIView) :
    authentication_classes = [ParentAuthentication]
    permission_classes = [ParentDataPermissions]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class ParentView (generics.GenericAPIView) :
    authentication_classes = [ListOfDataAuthentication , StudentAuthentication]
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    @swagger_auto_schema(
	operation_summary='Get data of student\'s parent',
	operation_description="""
	**send request that will read the parent of login student **
	that will retrieve the data of related parent data to student account which you are logged in  """, 
	responses={400:'not-found',
	403: 'unprocessable entity'},
	)
    def get (self , response , *args, **kwargs) : 
        try : 
            student = StudentActiveUsers.objects.get(authenticationKey = response.headers["Authorization"]).user
            parent_data = student.parent
            delattr (parent_data, "password")  
            parent_data = json.loads(serializers.serialize("json" , [parent_data , ]))
            return Response(parent_data[0])
        except Exception as ex : 
            return Response({"Message" : f" you are not Authenticated {str(ex)}"})

class StudentsView (generics.GenericAPIView) :
    authentication_classes = [ListOfDataAuthentication , ParentAuthentication]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    @swagger_auto_schema(
	operation_summary='Get data of parent\'s children',
	operation_description="""
	**send request that will read the children of login parent **
	that will retrieve the data of related children data to parent account which you are logged in  """, 
	responses={400:'not-found',
	403: 'unprocessable entity'},
	)
    def get (self , response , *args, **kwargs) : 
        try : 
            parent = ParentActiveUsers.objects.get(authenticationKey = response.headers["Authorization"]).user
            students_data = parent.children.all()
            parent_data = json.loads(serializers.serialize("json" , students_data))
            return Response(parent_data)
        except Exception as ex : 
            return Response({"Message" : "you are't have any children to view"})


class StudentLogin(generics.GenericAPIView) : 
    queryset = Student.objects.all()
    serializer_class = LoginSerializer
    @swagger_auto_schema(
	operation_summary='Login as Student',
	operation_description="""
	**send request with email and password**
	you will get authentication key that will used in header of any coming request use header name as **Authorization** """, 
	responses={400:'not-found',
	403: 'unprocessable entity'},
	)
    def post(self, request, *args, **kwargs):
        user = Student.objects.filter(Q(email=request.data["email"])&Q(password=request.data["password"])) 
        if len(user) > 0 : 
            now = datetime.now().strftime("%d/%m/%Y%H:%M:%S")
            request.data["dateTime"] = now 
            encoded_jwt = jwt.encode(request.data , "secret", algorithm="HS256")
            StudentActiveUsers.objects.create(authenticationKey = encoded_jwt , user = user[0] )
            return Response({"your authentication key is save it" : encoded_jwt})
        else  : 
            return Response({"Message" : "Wrong password or email"}) 
 
        
class StudentRegister(generics.GenericAPIView, mixins.CreateModelMixin ) :
   
        authentication_classes = [RegisterAuthentication]
        queryset = Parent.objects.all()
        serializer_class = StudentSerializer
        @swagger_auto_schema(
	    operation_summary='Register as student',
	    operation_description="""
	    **send request with student data**
	    that will create a new student ad store it in the database """, 
	    responses={400:'not-found',
	    403: 'unprocessable entity'},
	    )
        def post(self, request, *args, **kwargs):
            try : 
                return self.create(request, *args, **kwargs)
            except Exception as ex : 
                return Response({"status" : f"Wrong data as {str(ex)}"}) 
    
class StudentDetailView(generics.DestroyAPIView,generics.UpdateAPIView,generics.RetrieveAPIView) :
    authentication_classes = [StudentAuthentication]
    permission_classes = [StudentDataPermissions]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer