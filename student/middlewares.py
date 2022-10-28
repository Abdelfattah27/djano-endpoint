from rest_framework import authentication , permissions
from rest_framework import exceptions 
from .models import ParentActiveUsers, StudentActiveUsers

class ListOfDataAuthentication (authentication.BaseAuthentication) : 
    def authenticate (self , request , *args, **kwargs) :
        if request.method != "GET" :
            raise exceptions.AuthenticationFailed('you can only read data of your children')
        else :
            return (True , None)

class RegisterAuthentication(authentication.BaseAuthentication) : 
    def authenticate (self , request , *args, **kwargs) :
        if request.method != "POST" :
            raise exceptions.AuthenticationFailed('Wrong http method')
        else :
            return (True , None)


class ParentAuthentication (authentication.BaseAuthentication) : 
    def authenticate (self , request , *args, **kwargs) :
        if request.method == "POST" :
            raise exceptions.AuthenticationFailed('if you want to add user please go to "/register/" end point')
        authenticationKey = request.headers.get('Authorization') 
        authenticated = len(ParentActiveUsers.objects.filter(authenticationKey = authenticationKey)) > 0
        if authenticated : 
            return (True, None) 
        else :
            raise exceptions.AuthenticationFailed('you are not Authenticated please login in "/login/" end point') 

class StudentAuthentication (authentication.BaseAuthentication) : 
    def authenticate (self , request , *args, **kwargs) :
        if request.method == "POST" :
            raise exceptions.AuthenticationFailed('if you want to add user please go to "/parent/register/" end point')
        authenticationKey = request.headers.get('Authorization') 
        authenticated = len(StudentActiveUsers.objects.filter(authenticationKey = authenticationKey)) > 0
        if authenticated : 
            return (True, None) 
        else :
            raise exceptions.AuthenticationFailed('you are not Authenticated please login in "/login/" end point') 


class ParentDataPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        try : 
            parentActiveUser = ParentActiveUsers.objects.get(authenticationKey = request.headers.get("Authorization"))
            if view.kwargs.get('pk') == parentActiveUser.user.id : 
                return True 
            else : 
                self.message = 'You can\'t access this object'
                return False
        except Exception as ex : 
            self.message = f'Error happen while check your permission {str(ex)}'

    def has_object_permession(self, request, view, obj):
        return super().has_object_permession(request, view, obj)

class StudentDataPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        try : 
            parentActiveUser = StudentActiveUsers.objects.get(authenticationKey = request.headers.get("Authorization"))
            if view.kwargs.get('pk') == parentActiveUser.user.id : 
                return True 
            else : 
                self.message = 'You can\'t access this object'
                return False
        except Exception as ex : 
            self.message = 'Error happen while check your permission'

    def has_object_permession(self, request, view, obj):
        return super().has_object_permession(request, view, obj)