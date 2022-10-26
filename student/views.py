from django.shortcuts import render 
from .models import Student , Parent, Subject
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from .serializers import ParentSerializer, StudentSerializer, SubjectSerializer

import json
def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

class StudentView(APIView) : 
    def get(self , request) : 

        data = StudentSerializer(Student.objects.all() , many = True)
        return Response(data.data)

    def post(self , request) : 
        data = request.data
        serializer = StudentSerializer(data = data) 
        if serializer.is_valid() : 
            serializer.save() 
            return Response(serializer.data) 
        else : 
             return Response(serializer.errors)
class StudentDetailView(APIView): 
    def get(self , request , id) : 
        try : 
            data = StudentSerializer(Student.objects.get(id = id))
            return Response(data.data)
        except Student.DoesNotExist :
            return Response(status.HTTP_404_NOT_FOUND)
    def put(self, request, id) : 
        serializer = StudentSerializer(data=request.data, instance=Student.objects.get(id=id))
        if serializer.is_valid() : 
            serializer.save() 
            return Response(serializer.data) 
        else : 
            return Response(serializer.errors)  
    def delete(self, request, id): # no need for REST framework, endpoint GUT will have a DELETE button
        try: # use it to avoid get errors
            Student.objects.get(id=id).delete()
            return Response(status=status.HTTP_200_OK)
        except Student.DoesNotExist:
        	return Response(status.HTTP_404_NOT_FOUND)


class ParentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin  ) :
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer 
    def get(self, request, *args, **kwargs):
    	return self.list(request, *args, **kwargs)  
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
      

class ParentDetailView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin  ) :
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer 
    def put(self, request, *args, **kwargs):
	    return self.update(request, *args, **kwargs) 
    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
    	return self.retrieve(request, *args, **kwargs)
    
class SubjectDetailView(generics.DestroyAPIView,
				generics.UpdateAPIView,
				generics.RetrieveAPIView # needs id
				):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
class SubjectView(generics.ListCreateAPIView) :
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

